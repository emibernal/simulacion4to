import java.util.ArrayList;
import java.util.Scanner;

public class GeneradorCombinado {

    //Variables
    private int x;
    private int y;
    private int z;
    private int m;

    public GeneradorCombinado(int x, int y, int z, int m){
        this.x = x;
        this.y = y;
        this.z = z;
        this.m = m;
    }

    //Metodo principal 
    public int metodo(int x, int y, int z, int m){
        return ((x - y + z)) % m; 
    }

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);  
        //Ingreso la cantidad de generadores lineales que quiero tener
        System.out.print("Ingrese la cantidad de generadores lineales: ");
        int cant = sc.nextInt();
        //Ingreso la cantidad de numeros aleatorios
        System.out.print("Ingrese la cantidad de numeros aleatorios: ");
        int numCant = sc.nextInt();
        //Creo un arreglo para ir guardando los generadores
        ArrayList<GeneradorLineal> generadores = new ArrayList<>();
        
        //Itero guardando cada generador con su parametro
        for(int i = 0; i < cant; i++){
            System.out.print("Ingrese x0 para el generador " + (i+1) + ": ");
            int x = sc.nextInt();
            System.out.print("Ingrese a para el generador " + (i+1) + ": ");
            int a = sc.nextInt();
            System.out.print("Ingrese m para el generador " + (i+1) + ": ");
            int m = sc.nextInt();
            generadores.add(new GeneradorLineal(x, a, 0, m));
        }

        //Elijo el modulo que quiero usar para el combinado
        System.out.print("Que modulo usas para el generador combinado: ");
        int modulo = sc.nextInt();

        //Bucle por cada numero aleatorio que debo generar
        for(int j = 0; j < numCant; j++){
            long sumaCombinada = 0;

            //Cada generador labura
            for(int i = 0; i < generadores.size(); i++){
                //Obtengo el generador
                GeneradorLineal generador = generadores.get(i);
                //Calculo el numero
                int num = generador.method1(generador.getX(), generador.getA(), 0, generador.getM());
                
                //Calculo la logica de los signos por orden
                if(i % 2 == 0){
                    sumaCombinada += num;
                }else{
                    sumaCombinada -= num;
                }
            }

            //Ya tengo los 3 numeros por lo que aplico el modulo

            long res = sumaCombinada % modulo;
           
            // Ajuste por si el resultado es negativo o cero
            if (res <= 0) {
                res += modulo;
            }

            double u = (double) res / modulo;
            System.out.printf("Numero %d: %.4f%n", (j + 1), u);
        }


    }

    
}
