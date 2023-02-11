/*
 * Aquest programa implementa una calculadora bàsica
 *
 * Demana dos nombres per entrada estàndard i mostra el
 * resultat de sumar-los, restar-li el segon al primer, multiplicar-los,
 * dividir el primer entre el segon.
 *
 * El programa no controla valors no adequats d'entrada
 */

class CalculadoraBasica {
    public static void main(String[] args) {

        // obté operands d'entrada
        System.out.println("Primer operand:");
        int primerOperand = Integer.parseInt(Entrada.readLine());
        System.out.println("Segon operand:");
        int segonOperand = Integer.parseInt(Entrada.readLine());

        // operacions
        int suma = primerOperand + segonOperand;
        int resta = primerOperand - segonOperand;
        int multiplicacio = primerOperand * segonOperand;
        int divisio = primerOperand / segonOperand;

        // mostra resultats
        System.out.println("" + primerOperand + " + " + segonOperand + " = " + suma);
        System.out.println("" + primerOperand + " - " + segonOperand + " = " + resta);
        System.out.println("" + primerOperand + " x " + segonOperand + " = " + multiplicacio);
        System.out.println("" + primerOperand + " / " + segonOperand + " = " + divisio);
    }
}