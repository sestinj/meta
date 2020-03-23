async function asyncFunc() {
    let promise = new Promise((resolve, reject) => {
        setTimeout(() => resolve("done!"), 1000)
      });
      let result = await promise;
      return result;
}

function syncFunc() {
    var a = (async () => await asyncFunc())();
    return a;
}

console.log("S: " + syncFunc());