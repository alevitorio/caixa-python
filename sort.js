function sort(lista = [1, 2, 5, 3, 10, 7, 9, 4, 6]) {
    console.time()
  console.log("\nLIsta não ordenada \n[" + lista.join(" ") + "]\n");
  let trocas = 0;
 
  for (let i = 0; i < lista.length; i++) {
    for (let j = 0; j < lista.length - i - 1; j++) {
      if (lista[j] > lista[j + 1]) {
          console.log(
            `Lista[${j}] = ${lista[j]} > Lista[${j + 1}] = ${
              lista[j + 1]
            } vai trocar de posição: ${j} para ${j + 1} - [${lista}]`
          );
        let temp = lista[j];
        lista[j] = lista[j + 1];
        lista[j + 1] = temp;
        trocas++;

      } else {
        console.log(
          `Lista[${j}] = ${lista[j]} < Lista[${j + 1}] = ${
            lista[j + 1]
          } não vai trocar de posição ------- [${lista}]`
        );
      }
    }
  }
  console.log(
    "\nLIsta Ordenada - trocas: " + trocas + "\n[" + lista.join(" ") + "]\n"
  );
  console.timeEnd()
}

sort([33,5, 3, 8, 0, 2,9,15,-5,1,-10,6]);
console.time();
