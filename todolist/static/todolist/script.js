function setup() {
    $.ajaxSetup({
        headers: {"X-CSRFToken": $('[name=csrfmiddlewaretoken]').val()}
    });
    getTodolist();
}

/**
 * Retrieves and appends the user's todolist
 * to the page in the form of cards.
 */
function getTodolist() {
    $.getJSON("json", function(data) {
        var todolistHTML = '';
        $.each(data, function (key, task) {
                todolistHTML += getCard(task);
            });
        document.getElementById("data").innerHTML = todolistHTML;
    })
}

/**
 * 
 * @param {django model} task 
 * @returns Full Bootstrap Card of the task.
 */
function getCard(task) {
    item = `<div id="card-${task.pk}" class="card border-dark my-0.5 mx-0 col-xl-3 col-sm-6 text-start"> <div class="card-body">`;
    item += `<h2 class="card-title">${task.fields.task_name} </h2>`;
    item += `<p class="card-text">${task.fields.date}</p>`;
    item += `<p class="card-text">${task.fields.description}</p>`;
    if (task.fields.is_finished) {
        item += `</div> <div id="card-footer-${task.pk}" class="row row-cols-2 card-footer my-auto text-bg-success bg-opacity-75">`;
    } else {
        item += `</div> <div id="card-footer-${task.pk}" class="row row-cols-2 card-footer my-auto text-bg-secondary bg-opacity-75">`;
    }
    item += `<div class="col"> <button class="float-end btn btn-success btn-outline-dark" onclick="markAsDone(${task.pk})"type="submit">`
    item += `<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABmJLR0QA/wD/AP+gvaeTAAAAmklEQVRIie3SsQrCQBCE4fSpDdoLPqSvJfbaiIk2JuDb+Fl4QpCcemcjIQPb/Cyzw+4WxaRJ4xUqnLH7hueYtx46fuKp5jNcgskV83f8f8yD0TaYdKgC66+lffLcAWtsks2xx+m1AYchnpwc9VAjmghPW8vAkRYxnn3QkKrrpSojafMP2htywyqykt++BSWWkeFNqPxXnDQ+3QFgS6gRVorGfgAAAABJRU5ErkJggg==">`
    item += `</button></div>`;

    item += `<div class="col"> <button class="btn btn-danger btn-outline-dark" onclick="deleteTask(${task.pk})" type="submit">`
    item += `<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABmJLR0QA/wD/AP+gvaeTAAAAcUlEQVRIie2VzQ2AIAxGW+MW7sRMHh0U5niePIhoWtGokXcjKd8PByryC4CRLZPlrhbEqAmjqivNrkbsNMsbXDF/ewOTQZ7Q0/AdDZpBM2gGdfSWofwLzs9HPNYgicjgXD7JPAkEIBbW5B4RCI4wH2IGDpt3EfVw3qsAAAAASUVORK5CYII=">`
    item += `</button></div></div></div>`;

    return item;
}

/**
 * @param {form} taskForm 
 * Creates a POST request to submit the newly created task form and
 * appends a new card from the submitted data to the page.
 */
function submitNewTask(taskForm) {
    $.post("add", $(taskForm).serialize(), function(data){
        document.getElementById("data").innerHTML += getCard(data[0]);
        $('#newTaskModal').modal('hide');
        $('#emptyMsg').remove();
    });
}

/**
 * @param {int} id - task pk
 * Removes a task. (ft fade out)
 */
function deleteTask(id) {
    $.post(`delete-task/${id}`, $(taskForm).serialize(), function(){
        $(`#card-${id}`).fadeOut('slow');
    });
}

/**
 * @param {int} id - task pk
 * Marks a task done asynchronously.
 */
function markAsDone(id) {
    $.post(`finish-task/${id}`, $(taskForm).serialize(), function(){
        document.getElementById(`card-footer-${id}`).setAttribute('class', "row row-cols-2 card-footer my-auto text-bg-success bg-opacity-75");
    });
}

function logout() {
    $(location).attr('href', 'logout/');
}