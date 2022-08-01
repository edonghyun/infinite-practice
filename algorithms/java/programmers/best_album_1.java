import java.util.List;
import java.util.LinkedList;
import java.util.Map;
import java.util.HashMap;
import java.lang.Comparable;
import java.util.Collections;

class Solution {
    class GenreList {
        List<Genre> genreList = new LinkedList<>();
        Map<String, Genre> genreMap = new HashMap<>();
        
        public void add(String genreName) {
            if(genreMap.containsKey(genreName)) {
                return;
            }
            
            Genre genre = new Genre(genreName);
            genreList.add(genre);
            genreMap.put(genreName, genre);
        }
        
        public Genre get(String genreName) {
            return genreMap.get(genreName);
        }
    }
    
    class Genre implements Comparable<Genre> {
        String name;
        int totalPlays = 0;
        List<Song> songs = new LinkedList<>();

        Genre(String name) {
            this.name = name;
        }
        
        public void add(int i, int play) {
            totalPlays += play;
            Song song = new Song(i, play);
            songs.add(song);
            Collections.sort(songs);
        }
        
        public int compareTo(Genre o) {
            return o.totalPlays - this.totalPlays;
        };
    }
    
    class Song implements Comparable<Song> {
        int id;
        int play;
        
        Song(int id, int play) {
            this.id = id;
            this.play = play;
        }
        
        public int compareTo(Song o) {
            return this.play == o.play ?
                this.id - o.id :
                    o.play - this.play;
        };
    }

    public int[] solution(String[] genres, int[] plays) {
        int[] answer = {};
        
        GenreList genreList = new GenreList();
        for(int i = 0 ; i < genres.length; i ++) {
            String genreName = genres[i];
            int play = plays[i];

            genreList.add(genreName);
            Genre genre = genreList.get(genreName);
            genre.add(i, play);
        }
        
        List<Integer> result = new LinkedList<>();
        Collections.sort(genreList.genreList);
        for(Genre g : genreList.genreList) {
            int collectedCount = 0;
            for(Song s : g.songs) {
                if(collectedCount > 1) {
                    break;
                }
                result.add(s.id);
                collectedCount += 1;
            }
        }
        
        Integer[] r = result.toArray(new Integer[result.size()]);
        return result.stream().mapToInt(i->i).toArray();
    }
}