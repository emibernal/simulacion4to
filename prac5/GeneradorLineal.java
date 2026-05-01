
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class GeneradorLineal {

    //Variables
    private int x;
    private final int a;
    private final int c;
    private final int m;

    public GeneradorLineal(int x, int a, int c, int m){
        this.x = x;
        this.a = a;
        this.c = c;
        this.m = m;
    }

    //Metodo principal 
    public int method1(int x, int a, int c, int m){
        this.x = ((a * this.x) + c) % m; 
        return this.x;
    }

    //Getters 
    public int getA(){return a;}
    public int getX(){return x;}
    public int getC(){return c;}
    public int getM(){return m;}

    //Setter
    public void setX(int x){this.x = x;}

    @SuppressWarnings("ConvertToTryWithResources")
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Ingrese x0: ");
        int x = sc.nextInt();
        System.out.print("Ingrese a: ");
        int a = sc.nextInt();
        System.out.print("Ingrese c: ");
        int c = sc.nextInt();
        System.out.print("Ingrese m: ");
        int m = sc.nextInt();
        System.out.print("Ingrese cantidad de numeros: ");
        int cant = sc.nextInt();

        GeneradorLineal generadorLineal = new GeneradorLineal(x,a,c,m);

        try (PrintWriter writer = new PrintWriter(new FileWriter("numeros.txt"))) {
            int num = generadorLineal.method1(x, a, c, m);
            float real = (float) num/m;
            writer.println(real);
            System.out.println("Numero aleatorio 1: " + real);

            for(int i = 1; i < cant; i++){
                int res = generadorLineal.method1(num, a, c, m);
                real = (float) res/m;
                writer.println(real);
                System.out.println("Numero aleatorio " + (i+1) + ": " + real);
                num = res;
            }
            System.out.println("Archivo generado: numeros.txt");
        } catch (IOException e) {
            System.err.println("Error al escribir archivo: " + e.getMessage());
        }
        sc.close();
    }
}