document.getElementById("pt").addEventListener("click", project);
document.getElementById("create").addEventListener("click", create);
document.getElementById("st").addEventListener("click", statistic);

function statistic() {
    document.getElementById("kanban-board").classList.remove("show");
    document.getElementById("stats").classList.remove("hidden");
    document.getElementById("create").classList.remove("show");

    document.getElementById("kanban-board").classList.add("hidden");
    document.getElementById("stats").classList.add("show");
    document.getElementById("create").classList.add("hidden");
}

function project() {
    document.getElementById("kanban-board").classList.remove("hidden");
    document.getElementById("stats").classList.remove("show");
    document.getElementById("create").classList.remove("show");

    document.getElementById("kanban-board").classList.add("show");
    document.getElementById("stats").classList.add("hidden");
    document.getElementById("create").classList.add("hidden");
}

function create() {
    document.getElementById("kanban-board").classList.remove("show");
    document.getElementById("stats").classList.remove("show");
    document.getElementById("create").classList.remove("hidden");

    document.getElementById("kanban-board").classList.add("hidden");
    document.getElementById("stats").classList.add("hidden");
    document.getElementById("create").classList.add("show");
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function allowDrop(ev) {
    ev.preventDefault();
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.currentTarget.appendChild(document.getElementById(data));
}