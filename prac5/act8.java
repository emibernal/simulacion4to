import java.util.Random;

public class act8 {

    public static void main(String[] args){
        Random generadorUniforme = new Random();
        
        //Inicializamos las variables
        int n = 1000;
        double suma = 0;

        //Loop para generar los 1000 valores
        for(int i = 0; i < n; i++){
            double r = generadorUniforme.nextDouble();
            double x = 3 * Math.pow(r, 1.0/3.0);
            suma += x;

        }
        double mediaMuestra = suma / n;
        System.out.println("Media de la muestra obtenida: " + mediaMuestra);
    }

}
