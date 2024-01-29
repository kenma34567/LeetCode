class MyQueue {

    List<Integer> s1;
    List<Integer> s2;

    public MyQueue() {
        s1 = new ArrayList<Integer>();  // [1, 2]
        s2 = new ArrayList<Integer>();  //
    }

    public void push(int x) {
        s1.add(x);
        //System.out.println("pushed" + s1);
    }

    public int pop() {
        if (s2 == null || s2.size() == 0) {
            while (s1.size() > 0) {
                s2.add(s1.remove(s1.size()-1));
            }
        }
        return s2.remove(s2.size()-1);
    }

    public int peek() {
        if (s2 == null || s2.size() == 0) {
            while (s1.size() > 0) {
                s2.add(s1.remove(s1.size()-1));
            }
        }
        return s2.get(s2.size()-1);
    }

    public boolean empty() {
        return s1.size() == 0 && s2.size() == 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */