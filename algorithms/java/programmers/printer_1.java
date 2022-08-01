import java.util.Queue;
import java.util.LinkedList;

class Solution {
    class Element {
        int initialLocation;
        int priority;
        
        Element(int initialLocation, int priority) {
            this.initialLocation = initialLocation;
            this.priority = priority;
        }
    }

    public int solution(int[] priorities, int location) {
        int answer = 0;
        boolean biggerElementIsFound = false;
        
        Queue<Element> queue = new LinkedList<>();
        for(int i = 0; i < priorities.length; i ++) {
            Element element = new Element(i, priorities[i]);
            queue.add(element);
        }
        
        while(!queue.isEmpty()) {
            Element element = queue.poll();
            for(Element otherElement : queue) {
                if(element.priority < otherElement.priority) {
                    queue.add(element);
                    biggerElementIsFound = true;
                    break;
                }                
            }
            
            if(biggerElementIsFound) {
                biggerElementIsFound = false;
                continue;
            }
            
            answer += 1;
            if(element.initialLocation == location) {
                break;
            }
        }        
        
        return answer;
    }
}
