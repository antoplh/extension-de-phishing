chrome.tabs.query({active: true, currentWindow:true}, function(tabs){
  // get tab data
  var activeTab = tabs[0];
  var activeTabURL = activeTab.url;
  var activeTabURL = encodeURIComponent(activeTabURL)

  // call API
  //var apiCall = 'http://127.0.0.1:5000/result?url='+ activeTabURL;
  var apiCall = 'http://vfhurtadodemendozad.pythonanywhere.com/result?url=' + activeTab.url;
  
  fetch(apiCall, {mode:'cors'})
  .then(response => {
    if (response.status === 200) {
      console.log(response);
      response.json().then(data => ({
        data: data,
        status: response.status
      })).then(res => {
        console.log(res.status, res.data.result);
        document.getElementById("result").innerHTML = res.data.result;
	document.getElementById("proba_ph").innerHTML = res.data.proba_ph + '%';
	if(document.getElementById("result").innerHTML == "phishing"){
	document.getElementById("result").style.color = "red";}
	if(document.getElementById("result").innerHTML == "legitima"){
	document.getElementById("result").style.color = "green";}
      })
      
      return response.json();
    } else {
      console.log(response.statusText);
      document.getElementById("result").innerHTML = "hubo un error";
      throw new Error('Something went wrong on api server!');
    }
  })

});
