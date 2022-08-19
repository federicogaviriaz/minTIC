
class BecaUniversitaria {

    int pgTiempo;
    double pgMonto;
    double pgIntereses;

    public BecaUniversitaria(int pTiempo, double pMonto, double pInteres) {
        pgTiempo = pTiempo;
        pgMonto = pMonto;
        pgIntereses = pInteres;
    }

    public BecaUniversitaria() {
        pgTiempo = 0;
        pgMonto = 0;
        pgIntereses = 0;
    }

    public double calcularInteresSimple() {
        double simpCalc = Math.round(pgMonto * (pgIntereses / 100) * pgTiempo);
        return simpCalc;
    }

    public double calcularInteresCompuesto() {
        double compCalc = Math.round(pgMonto * (Math.pow((1 + pgIntereses / 100), pgTiempo) - 1));
        return compCalc;
    }

    public String compararInversion(int pTiempo, double pMonto, double pInteres) {
        pgTiempo = pTiempo;
        pgMonto = pMonto;
        pgIntereses = pInteres;
        double pComparacion = Math.round(calcularInteresCompuesto() - calcularInteresSimple());
        if (pgTiempo != 0 && pgMonto != 0 && pgIntereses != 0) {
            String sResult = "La diferencia entre la proyección de interés compuesto e interés simple es: $"
                    + pComparacion;
            return sResult;
        } else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }

    }

    public String compararInversion() {
        double pComparacion = Math.round(calcularInteresCompuesto() - calcularInteresSimple());
        if (pgTiempo != 0 && pgMonto != 0 && pgIntereses != 0) {
            String sResult = "La diferencia entre la proyección de interés compuesto e interés simple es: $"
                    + pComparacion;
            return sResult;
        } else {
            return "No se obtuvo diferencia entre las proyecciones, revisar los parámetros de entrada.";
        }
    }

}