class Node {
    int key;
    int value;
    Node prev;
    Node next;

    public Node(int key, int value) {
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    } 
}

class DoubleLinkedList {
    Node head;
    Node tail;

    public DoubleLinkedList(){
        head = new Node(0,0);
        head.next = tail;
        tail = new Node(0,0);
        tail.prev = head;
    }

    public void insertTail(Node newNode){
        newNode.next = tail;
        newNode.prev = tail.prev;
        tail.prev.next = newNode;
        tail.prev = newNode;
    }

    public void removeNode(Node n){
        n.prev.next = n.next;
        n.next.prev = n.prev;
    }

    public Node clearHead(){
        var tmp = head.next;
        this.removeNode(head.next);
        return tmp;
    }
}

class LRUCache {

    private final int capacity;
    private HashMap<Integer, Node> map;
    private DoubleLinkedList items;

    public LRUCache(int capacity) {
        map = new HashMap<>();
        items = new DoubleLinkedList();
        this.capacity = capacity;
    }
    
    public int get(int key) {
        var node = map.getOrDefault(key, null);
        if (node == null){
            return -1;
        }
        items.removeNode(node);
        items.insertTail(node);
        return node.value;

    }
    
    public void put(int key, int value) {
        if (map.containsKey(key)){
            items.removeNode(map.get(key));
        }
        var newNode = new Node(key, value);
        items.insertTail(newNode);
        map.put(key, newNode);
        if(map.size() > capacity){
            var head = items.clearHead();
            if (head != null) map.remove(head.key);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */