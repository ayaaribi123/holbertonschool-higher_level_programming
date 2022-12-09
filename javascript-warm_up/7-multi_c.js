#!/usr/bin/node
let i = 0
const num = parseInt(process.argv[2])
if (num)
{
	for(i; i < num; i++)
	{
		console.log("C is fun")
	}
}
	else 
	{
		console.log("Missing number of occurrences")
	}