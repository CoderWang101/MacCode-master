import org.apache.zookeeper.ZooDefs;
import org.apache.zookeeper.CreateMode;
import org.apache.zookeeper.ZooKeeper;

public class ZookeeperExample {
    private ZooKeeper zkClient;

    public ZookeeperExample(ZooKeeper zkClient) {
        this.zkClient = zkClient;
    }
    //假设 Zookeeper 集群已启动， 并且你已经通过 Zookeeper 客户端工具 （如 IDEA）
    //成功连接到 Zookeeper 服务端。请完成以下任务：

    // a. 创建永久节点 /Zdata 并设置节点数据为 zdata
    public void create() throws Exception {
        zkClient.create("/Zdata", 
                        "zdata".getBytes(), 
                        ZooDefs.Ids.OPEN_ACL_UNSAFE, 
                        CreateMode.PERSISTENT);
    }

    // b. 获取 /Zdata 节点的信息
    public void getZnode() throws Exception {
        byte[] data = zkClient.getData("/Zdata", false, null);
        String content = new String(data);
        System.out.println(content);
    }

    // c. 删除 /Zdata 节点信息
    public void remove() throws Exception {
        zkClient.delete("/Zdata", -1);
    }

//------------------------------------------------------------
    public static void main(String[] args) throws Exception {
        // 连接到 Zookeeper 服务端
        ZooKeeper zkClient = new ZooKeeper("localhost:2181", 30000, null);
        ZookeeperExample example = new ZookeeperExample(zkClient);

        // 创建节点
        example.create();

        // 获取节点数据
        example.getZnode();

        // 删除节点
        example.remove();

        // 关闭连接
        zkClient.close();
    }
}