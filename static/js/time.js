var numbers = {
  0: "০",
  1: "১",
  2: "২",
  3: "৩",
  4: "৪",
  5: "৫",
  6: "৬",
  7: "৭",
  8: "৮",
  9: "৯",
};

function replaceNumbers(a) {
      
  var output = '';
  input=a.toString();
  for (var i = 0; i < input.length; ++i) {
    
      output+=numbers[parseInt(input[i])];
  }
  
  return output;
}

function updateTime() {
  var today = new Date();
  var hour = today.getHours();
  var minute = today.getMinutes();
  var second = today.getSeconds();
  var prepand = hour >= 12 ? " PM " : " AM ";
  hour = hour >= 12 ? hour - 12 : hour;
  if (hour === 0 && prepand === " PM ") {
    if (minute === 0 && second === 0) {
      hour = 12;
      prepand = " দুপুর";
    } else {
      hour = 12;
      prepand = " PM";
    }
  }
  if (hour === 0 && prepand === " AM ") {
    if (minute === 0 && second === 0) {
      hour = 12;
      prepand = " রাত";
    } else {
      hour = 12;
      prepand = " AM";
    }
  }

  t_str = replaceNumbers(hour) + prepand + " : " + replaceNumbers(minute) + " : " + replaceNumbers(second);

  document.getElementById("time_span").innerHTML = t_str;
}

setInterval(updateTime, 1000);
