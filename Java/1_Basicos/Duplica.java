/*
 * Aquest programa duplica el valor que rep com a primer argument
 *
 * El programa no controla valors no adequats d'entrada
 */

class Duplica {
    public static void main(String[] args) {
        // declara les variables a utilitzar
        int nombreADuplicar;
        int nombreDuplicat;

        // obté el nombre a duplicar
        nombreADuplicar = 5;

        // calcula el doble
        nombreDuplicat = nombreADuplicar * 2;

        // mostra resultats
        System.out.print("El doble de ");
        System.out.print(nombreADuplicar);
        System.out.print(" és ");
        System.out.println(nombreDuplicat);
    }
}