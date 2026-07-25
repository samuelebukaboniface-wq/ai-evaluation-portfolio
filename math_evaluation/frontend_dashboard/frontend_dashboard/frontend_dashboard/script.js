const metrics=[
    {name:"Safety",score:95},
    {name:"Reasoning",score:92},
    {name:"Accuracy",score:90},
    {name:"Instruction Following",score:96}
];

const container=document.getElementById("metrics");

metrics.forEach(item=>{
    container.innerHTML+=`
    <div class="card">
        <h3>${item.name}</h3>
        <h2>${item.score}%</h2>
    </div>`;
});
