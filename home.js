async function updateUI(){
    const res = await fetch(`devices.json?cache=${Math.random}`);
    const d = await res.json();
    const descriptions = {
        on: "Active",
        off: "Idle",
        locked: "Secured",
        unlocked: "Open",
        opened: "Open",
        closed: "Closed",
    };

    const pillLabels ={
        on: "ON",
        off: "OFF",
        locked: "LOCKED",
        unlocked: "UNLOCKED",
        closed: "CLOSED",
        opened: "OPENED",
    };

    for (const [name, state] of Object.entries(d)){
        const el = document.getElementById(name);
        if(!el) continue;

        el.classList.remove("on","off","locked","unlocked","opened","closed");
        el.classList.add(state);

        const statusEl =el.querySelector(".device-status");
        if(statusEl){
            statusEl.textContent = descriptions[state] || state;
        }

        const pillEl = el.querySelector(".status-pill");
        if (pillEl){
            pillEl.textContent = pillLabels[state] || state.toUpperCase();
        }
    }
}

setInterval(updateUI,800);
updateUI();