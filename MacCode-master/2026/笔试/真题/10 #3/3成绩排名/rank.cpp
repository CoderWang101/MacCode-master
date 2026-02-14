#include <iostream>
#include <fstream>
using namespace std;

typedef struct Student
{
    string id; // 学号
    string name;
    int esource; // 英语成绩
    int csource; // 语文成绩
    int msource; // 数学成绩
    int sscoure; // 科学成绩
    int total;   // 总分

} student;

bool compare(const student &a, const student &b)
{
    return a.total > b.total;
}

int main()
{
    int n; // 学生人数/读取学生个数
    cout << "=====请输入学生人数：======" << endl;
    cin >> n;

    vector<student> students(n);
    ifstream file("students.txt");
    
    for (int i = 0; i < n; i++)
    {
        // 输入学生信息
        string name, id;
        int esource, csource, msource, sscoure;

        // FILE *file = fopen("students.txt", "r");
        // fscanf(file, "%s %s %d %d %d %d", &id, &name, &esource, &csource, &msource, &sscoure);
        
        file>>id >> name >> esource >> csource >> msource >> sscoure;

        students[i] = {id, name, esource, csource, msource, sscoure, esource + csource + msource + sscoure}; // 读取学生信息

        // 排序学生信息
        sort(students.begin(), students.end(), compare);
    }
    file.close();

    for (auto &s : students)
        cout << "学号：" << s.id << " 姓名：" << s.name << " 总分：" << s.total << endl;

    return 0;
}