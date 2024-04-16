function renderpage(id) {
    if (id == 0) {
        render0();
    }
    else if (id == 1) {
        render1();
    }
    else if (id == 2) {
        render2();
    }
    else if (id == 3) {
        render3();
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
                <div class="more-text"> 3. Buy or Sell?</div>
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
function render1() {
}
function render2() {
}
function render3() {
}


function goBack(id) {
    if (id == 0) {
        window.location.href = '/learn/15';
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
}
function goNext(id) {
    if (id == 0) {
        window.location.href = '/quiz/1';
    }
    else if (id == 1) {
        submitUserAnswer();
        window.location.href = '/quiz/2';
    }
    else if (id == 2) {
        submitUserAnswer();
        window.location.href = '/quiz/3';
    }
    else if (id == 3) {
        submitUserAnswer();
    }
}
function submitUserAnswer() {
    //ajas post request to submit user answer
}

$(document).ready(function() {
    renderpage(id);
});