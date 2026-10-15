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
        head = null;
        tail = null;
    }

    public Node clearHead(){
        var tmp = head;
        if (head == tail) {
            head = null;
            tail = null;
            return tmp;
        }
        if (head != null && head.next != null) head.next.prev = null;
        head = head == null ? null : head.next;
        return tmp;
    }

    public void insertTail(Node newTail){
        if (head == null && tail == null){
            head = newTail;
            tail = newTail;
            return;
        }
        tail.next = newTail;
        newTail.prev = tail;
        newTail.next = null;
        tail = newTail;
    }

    public void deleteElement(Node elem){
        if (elem == null) return;
        if (head == elem) head = (head == null) ? null : head.next;
        if (tail == elem) tail = (tail == null) ? null : tail.prev;
        if (elem.prev != null){
            elem.prev.next = elem.next;
        }
        if (elem.next != null){
            elem.next.prev = elem.prev;
        }
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
        items.deleteElement(node);
        items.insertTail(node);
        return node.value;

    }
    
    public void put(int key, int value) {
        if (map.containsKey(key)){
            items.deleteElement(map.get(key));
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