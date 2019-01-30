$(document).ready(function() {
  $(".submit-data").click(function(e) {
    e.preventDefault();
    let contact_data = {
      toNumber: $("#contact-number").val(),
      fromNumber: $("#from-number").val()
    };
    $.ajax({
      url: "/call",
      type: "POST",
      data: JSON.stringify(contact_data),
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      success: function(response) {
        alert(response);
      }
    });
  });
});
