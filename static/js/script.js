function startCourse() {
    let topic = document.getElementById("topic").value.trim();
    let days = document.getElementById("days").value.trim();
    let output = document.getElementById("curriculum");

    if (!topic || !days) {
        output.innerHTML = "Please enter both a topic and number of days.";
        return;
    }

    output.innerHTML = "Generating curriculum... Please wait.";

    fetch("/get_curriculum", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic, days })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            output.innerHTML = `<p style="color:red;">Error: ${data.error}</p>`;
        } else {
            output.innerHTML = `<pre>${data.curriculum}</pre>`;
        }
    })
    .catch(error => {
        output.innerHTML = `<p style="color:red;">Error: ${error.message}</p>`;
    });
}
