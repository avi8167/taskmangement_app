
// create_task api calling 

async function create(){

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const is_complete = document.getElementById("is_complete").checked;

    try {
        const response = await fetch("http://127.0.0.1:8000/tasks/create",{
            method:"POST",

            headers:{"Content-Type":"application/json"},

            body:JSON.stringify({
                title:title,
                description:description,
                is_complete:is_complete
            })
        });

        const data  = await response.json();

        console.log("Created task :",data)

        document.getElementById("title").value = "";
        document.getElementById("description") = "";
        document.getElementById("is_complete").checked = false;

        getTasks();

    }catch(error){
        console.error("Error",error)
    }

    
}


async function getTasks() {

    console.log("Getting tasks...");

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/tasks/all_tasks"
        );

        console.log("Status:", response.status);

        const data = await response.json();

        console.log("Data:", data);

        const taskList = document.getElementById("taskList");

        taskList.innerHTML = "";

        data.Data.forEach(function(task) {

            taskList.innerHTML += `
                <div>
                    <h3><b>${task.taskId}<b><h3>
                    <h2>${task.title}</h2>
                    <p>${task.description}</p>
                    <hr>
                </div>
            `;

        });

    } catch (error) {

        console.error("ERROR:", error);

    }
}

getTasks();

async function getOneTask() {

    const taskId = document.getElementById("taskId").value;

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/tasks/one_task/${taskId}`
        );

        const data = await response.json();

        console.log("One Task:", data);

        const oneTask = document.getElementById("oneTask");

        oneTask.innerHTML = `
            <div class="task">
                <h3>${data.title}</h3>
                <p>${data.description}</p>
            </div>
        `;

    } catch (error) {

        console.error("Error:", error);

    }
}


async function updateTask() {

    const taskId = document.getElementById("updateId").value;

    const title = document.getElementById("updateTitle").value;

    const description =
        document.getElementById("updateDescription").value;


    try {

        const response = await fetch(
            `http://127.0.0.1:8000/tasks/update_task/${taskId}`,
            {
                method: "PUT",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    title: title,
                    description: description
                })
            }
        );


        const data = await response.json();

        console.log("Updated Task:", data);


        // Clear inputs
        document.getElementById("updateId").value = "";

        document.getElementById("updateTitle").value = "";

        document.getElementById("updateDescription").value = "";


        // Refresh all tasks
        getTasks();

    } catch (error) {

        console.error("Error:", error);

    }
}

async function deleteTask() {
    const taskId = document.getElementById("deleteId").value;

    try {
        const response = await fetch(
            `http://127.0.0.1:8000/tasks/delete_task/${taskId}`,
            {
                method: "DELETE"
            }
        );

        const data = await response.json();

        console.log("Deleted Task:", data);

        document.getElementById("deleteId").value = "";

        // Refresh all tasks
        getTasks();

    } catch (error) {
        console.error("Error:", error);
    }
}