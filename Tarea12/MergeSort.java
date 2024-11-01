import java.util.Arrays;

public class MergeSort 
{

    public static void mergeSort(int[] data) 
    {
        if (data.length > 1) 
        {
            int mitad = data.length / 2;
            int[] izquierda = Arrays.copyOfRange(data, 0, mitad);
            int[] derecha = Arrays.copyOfRange(data, mitad, data.length);
            System.out.println(Arrays.toString(izquierda) + " --- " + Arrays.toString(derecha));
            mergeSort(izquierda);
            mergeSort(derecha);
            int i = 0;
            int d = 0;
            int k = 0;

            while (i < izquierda.length && d < derecha.length) 
            {
                if (izquierda[i] < derecha[d]) 
                {
                    data[k] = izquierda[i];
                    i++;
                } 

                else 
                {
                    data[k] = derecha[d];
                    d++;
                }

                k++;
            }

            while (i < izquierda.length) 
            {
                data[k] = izquierda[i];
                i++;
                k++;
            }

            while (d < derecha.length) 
            {
                data[k] = derecha[d];
                d++;
                k++;
            }
        }
        System.out.println("Regreso de rec: " + Arrays.toString(data));
    }

    public static void main(String[] args) 
    {
        int[] numeros = {38, 27, 43, 3, 9, 82, 10, 19, 50, 61};
        mergeSort(numeros);
        System.out.println("Arreglo ordenado:" + Arrays.toString(numeros));
    }
}
