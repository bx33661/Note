async function asyncOperation(): Promise<string> {
    return "Hello, async world!";
}
 
async function run() {
    const result = await asyncOperation();
    console.log(result);  // "Hello, async world!"
}
 
run();