import kotlin.math.max
import java.util.*
class MaximalRectangle {
    fun findMaxArea(data:IntArray):Int{
        var ans = 0
        var stack = Stack<Int>()
        var area = 0
        for(i in 0..data.size-1){
            var h = data[i]
            while (stack.size>0 && data[stack.last()]>=h){
                var n = stack.pop()
                if (stack.size>0){
                    area = data[n] * (i - stack.last()-1)
                }else{
                    area = data[n] * i
                }
                ans = max(area,ans)
            }
            stack.add(i)
        }
        //println("max area ${ans}")
        return ans
    }

    fun maximalRectangle(matrix: Array<CharArray>): Int {
        var m = matrix.size
        var n = matrix[0].size
        var row = IntArray(n+1)
        var ans = 0
        for(i in 0..m-1){
            if(i==0) {
                for (j in 0..n - 1) {
                    if (matrix[i][j]=='1')
                        row[j]=1
                }
            }else{
                for (j in 0..n - 1) {
                    if (matrix[i][j]=='1')
                        row[j]+=1
                    else
                        row[j]=0
                }
            }
            var area = findMaxArea(row)
            ans = max(ans, area)
        }

        return ans
    }
}
fun main(){
    var data:Array<CharArray> = arrayOf(
        charArrayOf('1','1','1','1','1'),
        charArrayOf('1','0','0','0','1'),
        charArrayOf('1','1','1','1','1'),
        charArrayOf('1','1','1','1','1')
    )
    var sol = MaximalRectangle()
    println(sol.maximalRectangle(data))
}
