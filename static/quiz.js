function renderpage(id, data) {
    if (id == 0) {
        render0();
    }
    else if (id == 1) {
        render1(data);
    }
    else if (id == 2) {
        render2(data);
    }
    else if (id == 3) {
        render3(data);
    }
    else if (id == 4) {
        render4(data);
    }
}

function render0() {
    let html = `
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="content-header"> Quiz </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <div class="some-text"> It is time to put your new knowledge to the test! This section will be a culmination of information that was taught throughout the website. This will be broken down into 3 different parts:</div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <div class="more-text"> 1.Identify the Chart </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <div class="more-text"> 2. Bearish or Bullish?</div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <div class="more-text more-pad"> 3. Buy or Sell?</div>
            </div>
        </div>
        <div class="row some-pad">
            <div class="col-md-4 center">
                <button class="btn btn-secondary" onclick="goBack(0)"> Previous </button>
            </div>
            <div class="col-md-4"></div>
            <div class="col-md-4 center">
                <button class="btn btn-success" onclick="goNext(0)"> Begin </button>
            </div>
        </div>
    </div>
    `;
    $('#content').html(html);
}
function render1(data) {
    let im1_src = data["1"];
    let im2_src = data["2"];
    let im3_src = data["3"];
    let dropdown_options = data["4"];
    let dropdown = `
                <select class="form-select" aria-label="Default select example">
                    <option selected disabled value="">Select an option</option>
                    <option value="1">${dropdown_options[0]}</option>
                    <option value="2">${dropdown_options[1]}</option>
                    <option value="3">${dropdown_options[2]}</option>
                    <option value="4">${dropdown_options[3]}</option>
                    <option value="5">${dropdown_options[4]}</option>
                </select>
    `;
    let html = `
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="content-header"> Identify the Chart </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-4 center">
                <img src="${im1_src}" class="img-fluid" alt="Image 1">
                ${dropdown}
            </div>
            <div class="col-md-4 center">
                <img src="${im2_src}" class="img-fluid" alt="Image 2">
                ${dropdown}
            </div>
            <div class="col-md-4 center">
                <img src="${im3_src}" class="img-fluid" alt="Image 3">
                ${dropdown}
            </div>
        </div>
        <div class="row some-pad">
            <div class="col-md-4 center">
                <button class="btn btn-secondary" onclick="goBack(1)"> Previous </button>
            </div>
            <div class="col-md-4"></div>
            <div class="col-md-4 center">
                <button class="btn btn-success" onclick="goNext(1)"> Submit </button>
            </div>
    </div>
    `;
    $('#content').html(html);
}
function render2(data) {
    let draggable_options = data["5"];
    let html = `
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="content-header"> Bearish or Bullish? </div>
            </div>
        </div>
        <div class="row" id= "add-after-here">
            <div class="col-md-3 center">
                <div class="draggable bordered" id="drag1">${draggable_options[0]}</div>
            </div>
            <div class="col-md-3 center">
                <div class="draggable bordered" id="drag2">${draggable_options[1]}</div>
            </div>
            <div class="col-md-3 center">
                <div class="draggable bordered" id="drag3">${draggable_options[2]}</div>
            </div>
            <div class="col-md-3 center">
                <div class="draggable bordered" id="drag4">${draggable_options[3]}</div>
            </div>
        </div>
        
        <div class="row">
            <div class="col-md-6">
                <div class="dropable bull bordered" id="drop1"></div>
                <div class="center big">Bullish</div>
            </div>
            <div class="col-md-6">
                <div class="dropable bear bordered" id="drop2"></div>
                <div class="center big">Bearish</div>
            </div>
        </div>
        <div class="row some-pad">
            <div class="col-md-4 center">
                <button class="btn btn-secondary" onclick="goBack(2)"> Previous </button>
            </div>
            <div class="col-md-4"></div>
            <div class="col-md-4 center">
                <button class="btn btn-success" onclick="goNext(2)"> Submit </button>
            </div>
        </div>
    `;
    $('#content').html(html);

    $( ".draggable" ).draggable({
        revert: 'invalid'
    });
    $( ".dropable" ).droppable({
        accept: '.draggable',
        drop: function(event, ui) {
            $(this).append(ui.draggable.css({
                position: 'relative',
                left: '0px',
                top: '0px'
            }));
        }
    });
}
function render3(data) {
    let im6_src = data["6"];
    let im7_src = data["7"];
    let html = `
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="content-header"> Buy or Sell? </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-6">
                <div class="row">
                    <div class="col-md-6 center">
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="image6" id="buyImage6" value="buy" checked>
                            <label class="form-check-label" for="buyImage6">Buy</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="image6" id="sellImage6" value="sell">
                            <label class="form-check-label" for="sellImage6">Sell</label>
                        </div>
                    </div>
                    <div class="col-md-6 center">
                        <img src="${im6_src}" class="img-fluid" alt="Image 6">
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="row">
                    <div class="col-md-6 center">
                        <img src="${im7_src}" class="img-fluid" alt="Image 7">
                    </div>
                    <div class="col-md-6 center">
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="image7" id="buyImage7" value="buy" checked>
                            <label class="form-check-label" for="buyImage7">Buy</label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="image7" id="sellImage7" value="sell">
                            <label class="form-check-label" for="sellImage7">Sell</label>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row some-pad">
            <div class="col-md-4 center">
                <button class="btn btn-secondary" onclick="goBack(3)"> Previous </button>
            </div>
            <div class="col-md-4"></div>
            <div class="col-md-4 center">
                <button class="btn btn-success" onclick="goNext(3)"> Submit </button>
            </div>
        </div>
    </div>
    `;
    $('#content').html(html);
}

function render4(data) {
    let score = data['8'];
    let html = `
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="content-header"> Your Score </div>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title text-center">Final Score</h5>
                        <p class="card-text text-center display-4">${score}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="row some-pad">
            <div class="col-md-4 center">
                <button class="btn btn-secondary" onclick="goBack(4)"> Previous </button>
            </div>
            <div class="col-md-4"></div>
            <div class="col-md-4 center">
                <button class="btn btn-success" onclick="goNext(4)"> Finish </button>
            </div>
        </div>
    </div>
    `;
    $('#content').html(html);
}

function goBack(id) {
    if (id == 0) {
        window.location.href = '/learn/12';
    }
    else if (id == 1) {
        window.location.href = '/quiz/0';
    }
    else if (id == 2) {
        window.location.href = '/quiz/1';
    }
    else if (id == 3) {
        window.location.href = '/quiz/2';
    }
    else if (id == 4) {
        window.location.href = '/quiz/3';
    }
}
function goNext(id) {
    if (id == 0) {
        window.location.href = '/quiz/1';
    }
    else if (id == 1) {
        if (submitUserAnswer(id)) {
            window.location.href = '/quiz/2';
        }
    }
    else if (id == 2) {
        if (submitUserAnswer(id)) {
        window.location.href = '/quiz/3';
        }
    }
    else if (id == 3) {
        if (submitUserAnswer(id)) {
        window.location.href = '/quiz/4';
        }
    }
    else if (id == 4) {
        submitUserAnswer(id)
    }
}
function submitUserAnswer(id) {
    if (!validityCheck(id)) {
        return false;
    }
    //ajas post request to submit user answer
    return true;
}

function validityCheck(id) {
    //check if user has selected an answer
    let isValid = true;
    if (id ==1) {
        // find all select elements
        let selects = document.getElementsByTagName('select');
        for (let i = 0; i < selects.length; i++) {
            if (selects[i].value == '') {
                // make red border around select element
                selects[i].style.border = "1px solid red";
                // add error message below select element if not already there
                let errorMessage = document.createElement('div');
                errorMessage.innerHTML = "Please select an option";
                if (selects[i].parentNode.getElementsByTagName('div').length == 0) {
                    selects[i].parentNode.appendChild(errorMessage);
                }
                isValid = false;
            }
            // remove error message if user selects an option
            // remove red border
            else {
                selects[i].style.border = "1px solid black";
                let errorMessage = selects[i].parentNode.getElementsByTagName('div');
                if (errorMessage.length > 0) {
                    selects[i].parentNode.removeChild(errorMessage[0]);
                }
            }
        }
    }
    else if (id == 2) {
        // check if user has dragged all options
        let drop1 = $('#drop1');
        let drop2 = $('#drop2');
        if (drop1.children().length + drop2.children().length < 4) {
            let errorMessage = `<div class="center error"> Please drag all options </div>`;

            // check if error message already exists
            if ($('#add-after-here').next().next().next().length == 0) {
                $('#add-after-here').after(errorMessage);
            }
            
            isValid = false;
        }
        else {
            // check if error message exists and remove it
            if ($('#add-after-here').next().next().next().length > 0) {
                $('#add-after-here').next().next().next().remove();
            }
        }
}
    return isValid;
}

$(document).ready(function() {
    renderpage(id, data);
});
