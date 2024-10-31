import java.io.FileReader;
import java.io.BufferedReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;

class tabelasHash {
    private static long contadorColisoes = 0;
    private static long contadorComparacoes = 0;
    private static Random randomizador = new Random();
    private static String CSV = "dadosHash.csv";
    private static String tempoInsercao;
    private static String tempoBusca;
    private static String funcaoHashUsada;
    private static int tamanhoTabela;
    private static int tamanhoConjunto;
    private static long seed = 123;

    public static int tamanhoArgs(String[] args) { // não pode usar .length
        int tamanhoArgs = 0;
        for (String arg : args) {
            tamanhoArgs++;
        }
        return tamanhoArgs;
    }

    public static void main(String[] args) {
        if (tamanhoArgs(args) >= 4) {
            seed = Long.parseLong(args[2]);
            randomizador.setSeed(seed);
            funcaoHashUsada = args[3];
        } else {
            System.out.println("Uso: java Hash <tamanhoConjunto> <tamanhoTabela> <seed> <funcaoHash>");
            return;
        }

        if (tamanhoArgs(args) >= 2) {
            tamanhoTabela = Integer.parseInt(args[1]);
        } else {
            tamanhoTabela = 100000;
        }

        if (tamanhoArgs(args) >= 1) {
            tamanhoConjunto = Integer.parseInt(args[0]);
        } else {
            tamanhoConjunto = 1000000;
        }

        Registro[] conjuntoDados = gerarConjuntoDados(tamanhoConjunto);
        MapaHash mapaHash = new MapaHash(tamanhoTabela);
        mapaHash.resetarContadores();
        long inicio = System.currentTimeMillis();

        for (Registro reg : conjuntoDados) {
            switch (funcaoHashUsada) {
                case "modulo":
                    mapaHash.inserirModulo(reg);
                    break;
                case "multiplicacao":
                    mapaHash.inserirMultiplicacao(reg);
                    break;
                case "dobra":
                    mapaHash.inserirDobra(reg);
                    break;
                default:
                    System.out.println("Função hash inválida.");
                    return;
            }
        }

        long fim = System.currentTimeMillis();
        tempoInsercao = (fim - inicio) + "ms";
        contadorColisoes = mapaHash.getContadorColisoes();

        int numBuscas = 5;
        int[] chavesBusca = new int[numBuscas];
        for (int i = 0; i < numBuscas; i++) {
            chavesBusca[i] = conjuntoDados[randomizador.nextInt(tamanhoConjunto)].id;
        }

        mapaHash.resetarContadores();
        inicio = System.currentTimeMillis();

        for (int chave : chavesBusca) {
            Registro resultado = null;
            switch (funcaoHashUsada) {
                case "modulo":
                    resultado = mapaHash.buscarModulo(chave);
                    break;
                case "multiplicacao":
                    resultado = mapaHash.buscarMultiplicacao(chave);
                    break;
                case "dobra":
                    resultado = mapaHash.buscarDobra(chave);
                    break;
            }
        }

        fim = System.currentTimeMillis();
        tempoBusca = (fim - inicio) + "ms";
        contadorComparacoes = mapaHash.getContadorComparacoes();

        escreverCSV(CSV);
        System.out.println("CSV salvo com a função hash: " + funcaoHashUsada);

    }

    public static Registro[] gerarConjuntoDados(int tamanho) {
        Registro[] conjunto = new Registro[tamanho];
        for (int i = 0; i < tamanho; i++) {
            int codigo = 100000000 + randomizador.nextInt(900000000); // Código de 9 dígitos
            conjunto[i] = new Registro(codigo);
        }
        return conjunto;
    }

    public static void escreverCSV(String CSV) {
        try {
            FileWriter arquivoCSV = new FileWriter(CSV, true);
            PrintWriter gravarArq = new PrintWriter(arquivoCSV);
            String primeiraLinha = null;
    
            if (arquivoCSV.equals(null)) {
                System.out.println("Arquivo não encontrado.");
            } else {
                FileReader leitor = new FileReader(CSV);
                BufferedReader leitorCSV = new BufferedReader(leitor);
                primeiraLinha = leitorCSV.readLine();
                leitor.close();
            }
    
            if (primeiraLinha == null) { // primeira linha do csv
                gravarArq.println("FuncaoHash,TamanhoConjunto,TamanhoTabela,TempoInsercao(ms),ColisoesInsercao,TempoBusca(ms),ComparacoesBusca");
            }
    
            gravarArq.println(funcaoHashUsada + "," + tamanhoConjunto + "," + tamanhoTabela + "," + tempoInsercao + ","
            + contadorColisoes + "," + tempoBusca + "," + contadorComparacoes);
            gravarArq.close();
            arquivoCSV.close();
    
            System.out.println("Arquivo CSV salvo com sucesso!");
        } catch (IOException e) {
            System.out.println("Erro ao criar arquivo CSV: " + e.getMessage());
        }
    }
}

class MapaHash {
    Lista[] lista;
    int tamanho;
    int contadorColisoes;
    int contadorComparacoes;

    MapaHash(int tamanho) {
        this.lista = new Lista[tamanho];
        this.tamanho = tamanho;
        this.contadorColisoes = 0;
        this.contadorComparacoes = 0;
        for (int i = 0; i < tamanho; i++) {
            lista[i] = new Lista();
        }
    }

    // modulo
    public void inserirModulo(Registro reg) {
        int valor = reg.id % tamanho;
        if (!lista[valor].vazio()) {
            contadorColisoes++;
        }
        lista[valor].adicionarFinal(reg);
    }

    public Registro buscarModulo(int id) {
        int valor = id % tamanho;
        Lista bucket = lista[valor];
        ListaItem atual = bucket.getPrimeiroItem();
        while (atual != null) {
            contadorComparacoes++;
            if (atual.item.id == id) {
                return atual.item;
            }
            atual = atual.proximo;
        }
        return null;
    }

    public void inserirMultiplicacao(Registro reg) {
        int valor = hashMultiplicacao(reg.id);
        if (!lista[valor].vazio()) {
            contadorColisoes++;
        }
        lista[valor].adicionarFinal(reg);
    }

    public Registro buscarMultiplicacao(int id) {
        int valor = hashMultiplicacao(id);
        Lista bucket = lista[valor];
        ListaItem atual = bucket.getPrimeiroItem();
        while (atual != null) {
            contadorComparacoes++;
            if (atual.item.id == id) {
                return atual.item;
            }
            atual = atual.proximo;
        }
        return null;
    }

    public void inserirDobra(Registro reg) {
        int valor = hashDobra(reg.id);
        if (!lista[valor].vazio()) {
            contadorColisoes++;
        }
        lista[valor].adicionarFinal(reg);
    }

    public Registro buscarDobra(int id) {
        int valor = hashDobra(id);
        Lista bucket = lista[valor];
        ListaItem atual = bucket.getPrimeiroItem();
        while (atual != null) {
            contadorComparacoes++;
            if (atual.item.id == id) {
                return atual.item;
            }
            atual = atual.proximo;
        }
        return null;
    }

    // multiplicação
    private int hashMultiplicacao(int chave) {
        double A = 0.6180339887; // Parte fracionária da razão áurea
        double resultado = chave * A;
        resultado = resultado - Math.floor(resultado);
        return (int) (tamanho * resultado);
    }

    // dobramento
    private int hashDobra(int chave) {
        String chaveStr = String.valueOf(chave);
        int soma = 0;
        for (int i = 0; i < chaveStr.length(); i += 3) {
            String parte = chaveStr.substring(i, Math.min(i + 3, chaveStr.length()));
            soma += Integer.parseInt(parte);
        }
        return soma % tamanho;
    }

    // Métodos para gerenciar contadores
    public void resetarContadores() {
        contadorColisoes = 0;
        contadorComparacoes = 0;
    }

    public int getContadorColisoes() {
        return contadorColisoes;
    }

    public int getContadorComparacoes() {
        return contadorComparacoes;
    }
}

class Lista {
    private int tamanho;
    private ListaItem primeiro;

    Lista() {
        tamanho = 0;
        primeiro = null;
    }

    boolean vazio() {
        return primeiro == null;
    }

    int getTamanho() {
        return tamanho;
    }

    ListaItem getPrimeiroItem() {
        return primeiro;
    }

    void adicionarFinal(Registro item) {
        tamanho++;
        ListaItem novo = new ListaItem(item);
        if (vazio()) {
            primeiro = novo;
            return;
        }
        ListaItem l = primeiro;
        while (l.proximo != null) {
            l = l.proximo;
        }
        l.proximo = novo;
    }
}

class ListaItem {
    Registro item;
    ListaItem proximo;

    ListaItem(Registro item) {
        this.item = item;
        proximo = null;
    }

    public String toString() {
        return item.toString();
    }
}

class Registro {
    int id;

    Registro(int id) {
        this.id = id;
    }

    public String toString() {
        return String.format("%d", id);
    }
}
