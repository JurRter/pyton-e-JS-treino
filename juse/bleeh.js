const prompt = require('prompt-sync')({ sigint: true });

console.log('hellooo');
function soma(a, b) {
    return a + b;
}

function calculadora() {
    while (true) {
        console.log("Escolha a operação:");
        console.log("1. Soma");
        console.log("2. Subtração");
        console.log("3. Multiplicação");
        console.log("4. Divisão");
        console.log("5. Potenciação");
        console.log("6. Raiz");
        console.log("7. Sair");
        const escolha = prompt("Digite o número da operação desejada: ");
        if (escolha === '7') {
            console.log("Encerrando a calculadora.");
            break;
        }
        const num1 = parseFloat(prompt("Digite o primeiro número: "));
        let num2;
        if (escolha === '5') {
            num2 = parseFloat(prompt("Digite o expoente: "));
        } else if (escolha === '6') {
            num2 = parseFloat(prompt("Digite o índice da raiz: "));
        }
        else {
            num2 = parseFloat(prompt("Digite o segundo número: "));
        }
        let resultado;
        switch (escolha) {
            case '1':
                resultado = num1 + num2;
                break;
            case '2':
                resultado = num1 - num2;
                break;
            case '3':
                resultado = num1 * num2;
                break;
            case '4':
                resultado = num1 / num2;
                break;
            case '5':
                resultado = Math.pow(num1, num2);
                break;
            case '6':
                resultado = Math.pow(num1, 1 / num2);
                break;
            default:
                console.log("Operação inválida.");
                continue;
        }
        console.log(`O resultado é: ${resultado}`);
    }
}
calculadora();
