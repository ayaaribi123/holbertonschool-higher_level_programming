#!/usr/bin/node
function add(a,b){
const a = parseInt(process.argv[2])
const b = parseInt(process.argv[3])
if(isNaN(process.argv[2]))
{
console.log("NaN")
}
else
{
	console.log(a + b)
}
}