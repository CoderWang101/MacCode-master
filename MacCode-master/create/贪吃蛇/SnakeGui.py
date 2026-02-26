import tkinter as tk
import subprocess
import threading
import queue
import time
import os
import sys
import json
from datetime import datetime

# 贪吃蛇前端 GUI (Python/Tkinter)
# 调用 SnakeBackend 可执行文件作为游戏引擎

HIGHSCORE_FILE = "highscore.json"

class SnakeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.resizable(False, False)
        
        # 默认配置
        self.width = 20
        self.height = 20
        self.cell_size = 25
        
        # 游戏状态
        self.process = None
        self.running = False
        self.queue = queue.Queue()
        self.score = 0
        self.game_state = 0
        self.map_data = []
        
        # 最高分数据
        self.high_score = 0
        self.high_score_time = "None"
        self.load_high_score()
        
        # 主容器
        self.main_frame = tk.Frame(master, padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.show_start_screen()

    def load_high_score(self):
        if os.path.exists(HIGHSCORE_FILE):
            try:
                with open(HIGHSCORE_FILE, 'r') as f:
                    data = json.load(f)
                    self.high_score = data.get("score", 0)
                    self.high_score_time = data.get("time", "None")
            except:
                pass

    def save_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            self.high_score_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            try:
                with open(HIGHSCORE_FILE, 'w') as f:
                    json.dump({"score": self.high_score, "time": self.high_score_time}, f)
            except:
                pass
            return True
        return False

    def show_start_screen(self):
        # 清理界面
        self.clear_frame()
        self.master.unbind("<Key>")
        
        # 标题
        tk.Label(self.main_frame, text="Snake Game", font=("Helvetica", 32, "bold")).pack(pady=(0, 20))
        
        # 历史最高分
        score_frame = tk.Frame(self.main_frame, relief=tk.GROOVE, borderwidth=2, padx=10, pady=10)
        score_frame.pack(pady=10, fill=tk.X)
        
        tk.Label(score_frame, text="🏆 High Score", font=("Arial", 14, "bold"), fg="#FFD700").pack()
        tk.Label(score_frame, text=f"{self.high_score}", font=("Arial", 24, "bold")).pack()
        tk.Label(score_frame, text=f"Date: {self.high_score_time}", font=("Arial", 10), fg="gray").pack()
        
        # 按钮区
        btn_frame = tk.Frame(self.main_frame)
        btn_frame.pack(pady=30)
        
        tk.Button(btn_frame, text="Start Game", command=self.start_game, 
                 font=("Arial", 16), width=15, bg="#4CAF50", fg="black").pack(pady=10)
        
        tk.Button(btn_frame, text="Quit", command=self.master.quit, 
                 font=("Arial", 16), width=15, bg="#f44336", fg="black").pack(pady=10)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def start_game(self):
        self.clear_frame()
        
        # 启动后端
        if not self.start_backend():
            return
            
        # 游戏UI
        header_frame = tk.Frame(self.main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.score_label = tk.Label(header_frame, text="Score: 0", font=("Arial", 16, "bold"))
        self.score_label.pack(side=tk.LEFT)
        
        tk.Label(header_frame, text="Press Q to Quit", font=("Arial", 10), fg="gray").pack(side=tk.RIGHT)
        
        self.canvas_width = self.width * self.cell_size
        self.canvas_height = self.height * self.cell_size
        self.canvas = tk.Canvas(self.main_frame, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()
        
        # 绑定按键
        self.master.bind("<Key>", self.on_key_press)
        self.master.focus_set()
        
        # 启动循环
        self.running = True
        self.read_thread = threading.Thread(target=self.read_backend_output, daemon=True)
        self.read_thread.start()
        
        self.update_gui()

    def get_resource_path(self, relative_path):
        """ 获取资源绝对路径，兼容开发环境和 PyInstaller 打包环境 """
        if hasattr(sys, '_MEIPASS'):
            # PyInstaller 创建临时文件夹并将路径存储在 _MEIPASS 中
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def start_backend(self):
        backend_path = self.get_resource_path("SnakeBackend")
        
        if not os.path.exists(backend_path):
            tk.Label(self.main_frame, text=f"Error: Backend not found at {backend_path}", fg="red").pack()
            return False

        try:
            self.process = subprocess.Popen(
                [backend_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            
            # 读取初始化信息
            line = self.process.stdout.readline()
            if line.startswith("INIT"):
                parts = line.split()
                self.width = int(parts[1])
                self.height = int(parts[2])
                return True
            else:
                print(f"Unexpected init line: {line}")
                return False
        except Exception as e:
            print(f"Start backend error: {e}")
            return False

    def stop_backend(self):
        self.running = False
        if self.process:
            try:
                self.process.stdin.write('q')
                self.process.stdin.flush()
            except:
                pass
            self.process.terminate()
            self.process = None

    def read_backend_output(self):
        buffer = []
        capturing = False
        
        while self.running and self.process and self.process.poll() is None:
            try:
                line = self.process.stdout.readline()
                if not line: break
                
                line = line.strip()
                if line == "FRAME_START":
                    buffer = []
                    capturing = True
                elif line == "FRAME_END":
                    if capturing:
                        self.queue.put(buffer)
                        capturing = False
                elif capturing:
                    buffer.append(line)
            except:
                break

    def update_gui(self):
        try:
            latest_frame = None
            while not self.queue.empty():
                latest_frame = self.queue.get_nowait()
            
            if latest_frame:
                self.parse_frame(latest_frame)
                self.draw()
                
                if self.game_state != 0: # Game Over or Victory
                    self.handle_game_over()
                    return # Stop updating
                    
        except queue.Empty:
            pass
        
        if self.running:
            self.master.after(20, self.update_gui)

    def parse_frame(self, lines):
        for line in lines:
            if line.startswith("SCORE"):
                self.score = int(line.split()[1])
            elif line.startswith("STATE"):
                self.game_state = int(line.split()[1])
            elif line.startswith("MAP"):
                raw_map = line.split()[1] if len(line.split()) > 1 else ""
                self.map_data = [int(c) for c in raw_map]

    def draw(self):
        self.canvas.delete("all")
        
        # 绘制地图
        for i, val in enumerate(self.map_data):
            if val == 0: continue
            
            x = (i % self.width) * self.cell_size
            y = (i // self.width) * self.cell_size
            
            if val == 1: # Snake
                self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill="#4CAF50", outline="#388E3C")
            elif val == 2: # Food
                self.canvas.create_oval(x+2, y+2, x + self.cell_size-2, y + self.cell_size-2, fill="#F44336", outline="#D32F2F")

        self.score_label.config(text=f"Score: {self.score}")

    def handle_game_over(self):
        self.running = False
        
        # 绘制半透明遮罩 (模拟)
        self.canvas.create_rectangle(0, 0, self.canvas_width, self.canvas_height, fill="black", stipple="gray50")
        
        # 游戏结束文本
        self.canvas.create_text(self.canvas_width/2, self.canvas_height/2 - 40, 
                               text="GAME OVER", fill="white", font=("Arial", 30, "bold"))
        
        # 检查是否打破记录
        is_new_record = self.save_high_score(self.score)
        if is_new_record:
            self.canvas.create_text(self.canvas_width/2, self.canvas_height/2, 
                                   text="🏆 NEW HIGH SCORE! 🏆", fill="gold", font=("Arial", 18, "bold"))
        else:
            self.canvas.create_text(self.canvas_width/2, self.canvas_height/2, 
                                   text=f"Final Score: {self.score}", fill="white", font=("Arial", 16))
            
        # 添加按钮
        btn_restart = tk.Button(self.main_frame, text="Play Again", command=self.restart_game, 
                               font=("Arial", 14), bg="white", fg="black")
        self.canvas.create_window(self.canvas_width/2, self.canvas_height/2 + 50, window=btn_restart)
        
        btn_menu = tk.Button(self.main_frame, text="Main Menu", command=self.return_to_menu, 
                            font=("Arial", 14), bg="white", fg="black")
        self.canvas.create_window(self.canvas_width/2, self.canvas_height/2 + 100, window=btn_menu)

    def on_key_press(self, event):
        if not self.running: return
        
        key = event.keysym.lower()
        cmd = ''
        if key == 'w' or key == 'up': cmd = 'w'
        elif key == 's' or key == 'down': cmd = 's'
        elif key == 'a' or key == 'left': cmd = 'a'
        elif key == 'd' or key == 'right': cmd = 'd'
        elif key == 'q': 
            self.return_to_menu()
            return
            
        if cmd and self.process:
            try:
                self.process.stdin.write(cmd)
                self.process.stdin.flush()
            except:
                pass

    def restart_game(self):
        self.stop_backend()
        self.start_game()

    def return_to_menu(self):
        self.stop_backend()
        self.show_start_screen()

if __name__ == "__main__":
    root = tk.Tk()
    # 设置窗口居中
    root.update_idletasks()
    width = 600
    height = 700
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    
    game = SnakeGUI(root)
    root.mainloop()
