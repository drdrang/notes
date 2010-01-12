function styleLN() {
  var preElems = document.getElementsByTagName('pre');
  if (0 == preElems.length) {   // no pre elements; stop
     return;
  }
  for (var i = 0; i < preElems.length; i++) {
    var pre = preElems[i];
    var code = pre.getElementsByTagName('code')[0];
    if (null == code) {        // no code; move on
      continue;
    }
    var oldContent = code.innerHTML;
    var newContent = oldContent.replace(/^( *)(\d+):(  )/mg, 
               '<span class="ln">$1$2$3<' + '/span>');
    if (oldContent.match(/^( *)(\d+):(  )/mg)) {
      newContent += "\n" + '<button onclick="toggleLN(this.parentNode)">Toggle line numbers</button>';
    }
    code.innerHTML = newContent;
  }
}

function toggleLN(code) {
  for (var i=0; i<code.childNodes.length; i++){
    node = code.childNodes[i];
    if (node.nodeName == 'SPAN'){
      if (node.style.display == 'none') node.style.display = '';
      else node.style.display = 'none';
    }
  }
}
