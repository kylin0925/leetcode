class Solution {
    fun minOperations(boxes: String): IntArray {
        var ans = IntArray(boxes.length)
        var one = 0
        var cnt = 0
        
        for(i in 0..boxes.length-1){
            ans[i]+=cnt
            if(boxes[i] == '1')
            	one+=1
            cnt+=one
        }
        one = 0
        cnt = 0
        for(i in boxes.length-1 downTo 0){
            ans[i]+=cnt
            if(boxes[i] == '1')
            	one+=1
            cnt+=one
        }
        	
        return ans
    }
}