import java.util.*;
import java.util.stream.Collectors;
class Solution {
    
    static int row;
    static int col;
    static char [][] grid;
    
    public void init(String[] storage, String[] requests){
        row = storage.length+2;
        col = storage[0].length()+2;
        grid = new char [row][col];
        for(int i = 0; i<row; i++){
            Arrays.fill(grid[i],'*');
        }
        for(int i = 1; i<row-1; i++){
            for(int j = 1; j < col-1; j++){
                grid[i][j] = storage[i-1].charAt(j-1);
            }
        }
    }
    
    public void print(){
        Arrays.stream(grid)
            .map(r -> new String(r))
            .forEach(System.out::println);
    }
    
    public void bfs(char target){
        boolean[][] visited = new boolean [row][col];
        boolean[][] changed = new boolean [row][col];
        ArrayDeque<int[]> q = new ArrayDeque<>();
        int[][] dirs = {{-1,0},{0,-1},{1,0},{0,1}};
        q.add(new int[] {0,0});
        visited[0][0] = true;
        
        while(!q.isEmpty()){
            int[] t = q.pollFirst();
            for(int i =0; i<4; i++){
                int nr = dirs[i][0] + t[0];
                int nc = dirs[i][1] + t[1];
                if (
                    0<=nr && nr < row && 0<=nc && nc < col
                    && !visited[nr][nc] && !changed[nr][nc] && (grid[nr][nc]=='*' || grid[nr][nc]==target)
                ){
                    if(grid[nr][nc]==target){
                        grid[nr][nc] = '*';
                        changed[nr][nc] =true;
                    }
                    if(!changed[nr][nc]){
                        q.add(new int[] {nr,nc});
                        visited[nr][nc] = true;   
                    }
                }
            }
        }
    }
    
    public void delAll(char target){
        for(int i = 1; i<row-1; i++){
            for(int j = 1; j<col-1; j++){
                if(grid[i][j] == target){
                    grid[i][j] = '*';
                }
            }
        }
    }
    
    public int solution(String[] storage, String[] requests) {
        int answer = 0;
        init(storage, requests);
        for(String r : requests){
            if(r.length() == 1){
                bfs(r.charAt(0));
            }else{
                delAll(r.charAt(0));
            }
        }
        // print(); 
        for(int i = 1; i<row-1; i++){
            for(int j = 1; j<col-1; j++){
                if(grid[i][j] != '*'){
                    answer += 1;
                }
            }
        }
        
        return answer;
    }
}