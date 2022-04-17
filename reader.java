import java.io.BufferedReader;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.*; 

public class reader {
    public static void main(String[] args) throws IOException{
        // BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        // try{
        //     Boolean x =Boolean.parseBoolean(bf.readLine());
        //     //String str = bf.readLine();
        //     System.out.println(x);
        // }
        // catch(IOException e){
        //     System.out.println(e);
        // }

        // Scanner scanner = new Scanner(System.in);
        // int y = scanner.nextInt();
        // System.out.println(y);

        File file = new File("yoink.txt");
        //FileWriter fileWriter = new FileWriter(file, true);
        BufferedWriter bw = new BufferedWriter(new FileWriter(file, true));
        bw.append("yoink\n");
        bw.append("yee\n");
        bw.close();

        // reading text file using buffered reader and file reader
        System.out.println("buffered reader");
        BufferedReader br = new BufferedReader(new FileReader("example.txt") );
        // this variable points to the buffered line
        String line;
        // Keep buffering the lines and print it.
        while ((line = br.readLine()) != null) {
            System.out.println(line);
        }

        // reading textfile only using file reader
        System.out.println("\nfile reader");
        FileReader fr=new FileReader("example.txt");    
        int i;    
        while((i=fr.read())!=-1) {
            System.out.print((char)i);
        } 
        fr.close();    

        // reading using file input stream
        System.out.println("\n\nfile input stream");
        FileInputStream fs = new FileInputStream("example.txt");
        int j;
        while((j = fs.read()) != -1) {
            System.out.print((char)j);
        }
        
        ArrayList<String> arrayList = new ArrayList<String>();
        arrayList.add("yum");
        arrayList.add("hi");
        arrayList.add("dog");
        arrayList.add("hi");
        System.out.println(arrayList);
        arrayList.remove("hi");
        System.out.println(arrayList);
        arrayList.remove(0);
        System.out.println(arrayList);
        System.out.println(arrayList.contains("dog"));
    }
}
