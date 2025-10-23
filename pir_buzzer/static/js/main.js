let aliveSecond = 0;
let heartBeatRate = 5000;

function time()
{
	let d = new Date();
	let currentSecond = d.getTime();
	if(currentSecond - aliveSecond > heartBeatRate + 1000)
	{
		document.getElementById("connection_id").innerHTML = "DEAD";
	}
	else
	{
		document.getElementById("connection_id").innerHTML = "ALIVE";
	}
	setTimeout('time()', heartBeatRate);
}

function keepAlive()
{
	fetch('/keep_alive')
	.then(response=>{
		if(response.ok){
			let date = new Date();
			aliveSecond = date.getTime();
			return response.json();
		}
		throw new Error("Server offline");
	})
	.then(responseJson=>{
		if(reponseJson.motion == 1)
		{
			document.getElementById("motion_id").innerHTML="Motion";
		}
		else
		{
			document.getElementById("motion_id").innerHTML="No Motion";
		}
	})
	.catch(error=>console.log(error));
	setTimeout('keepAlive()', heartBeatRate);
}

function sendEvent(value)
{
	fetch("/status="+value,
	{
		method:"POST",
	})
}

function handleClick(cb)
{
	if(cb.checked)
	{
		value = "on";
	}
	else
	{
		value = "off";
	}
	sendEvent(cb.id+"-"+value);
}

