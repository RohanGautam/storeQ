const uploadButton = document.getElementById("uploadButton")
const downloadButton = document.getElementById("downloadButton")
const uploadProgress = document.getElementById("uploadProgress")
const downloadProgress = document.getElementById("downloadProgress")

const LOCAL_URL = "http://127.0.0.1:5000";

countUpload=0
function updateUpload() {
    if(countUpload<100){
        countUpload+=20;
    }
    uploadProgress.value = countUpload;
    setTimeout(updateUpload,1000)
}

countDownload=0
function updateDownload() {
    if(countDownload<100){
        countDownload+=2;
    } else if (countDownload>=100){
        var result = document.getElementById('renderResult');
        img = document.createElement('img')
        img.src = "../img/result2.png"
        result.appendChild(img)
    }
    downloadProgress.value = countDownload;
    setTimeout(updateUpload,1000)
}




async function startUpload() {
    updateUpload();
    const url = `${LOCAL_URL}/startUpload`
    fetch(url, {mode: 'cors'});
}

async function startDownload() {
    updateDownload();
    const url = `${LOCAL_URL}/startDownload`
    fetch(url, {mode: 'cors'});    
}

uploadButton.onclick = startUpload; 
downloadButton.onclick = startDownload; 