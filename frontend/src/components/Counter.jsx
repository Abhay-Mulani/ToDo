import React, { useState } from 'react';

function Counter() {
	let [i,setI] = useState(0); // state
	console.log('Counter Component rendering started',i);
	function incrementI(){ // update state
		//i = i + 2;
		setI(i+2); //setName("Pranjal") 
	}
	//incrementI();
	return (
		<div>
			<p>hello from Counter component</p>
			{/*
			<p id="i_value1">{i}</p>
			<p id="i_value2">{i}</p>
			*/}
			<p>{i}</p>
			<button onClick={incrementI}>increment I</button>
			<p>{i}</p>
		</div>
	)
}

export default Counter