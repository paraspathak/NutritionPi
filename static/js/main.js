$(document).ready(function () {
    $.ajax({
        url: '/takephoto',
        type: 'POST',
        data: JSON.stringify('start'),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function (msg) {
            console.log(msg);
            // data = JSON.parse(msg);
            $('#add_here').append(genereate_nutrition(msg));
            tag = `<img src="static/img/`+msg['image']+`" alt={{ employee.name }} width="512" height="360" />`
            console.log(tag);
            $('#add_image').append(tag);
        }
    });
    
    
}); 

function genereate_nutrition(data){
    document.getElementById("food").innerHTML= data['food_name'];
    var row = `<table class="table table-hover">
    <tbody>
      <tr>
      <td class = "col-4"> Total fat: </td>
      <td class = "col-2 align_me" >`+ data['nf_total_fat'] +` </td>
      </tr>
      <tr>
      <td class = "col-4">Saturated fat:</td>
      <td class = "col-2 align_me" >`+ data['nf_saturated_fat'] +` </td>
      </tr>
      <tr>
      <td class = "col-4">Cholesterol:</td>
      <td class = "col-2 align_me" >`+ data['nf_cholesterol'] +` </td>
      </tr>
      <tr>
      <td class = "col-4">Sodium:</td>
      <td class = "col-2 align_me" >`+ data['nf_sodium'] +` </td>
      </tr>
      <tr>
      <td class = "col-4">Total Carbs:</td>
      <td class = "col-2 align_me" >`+ data['nf_total_carbohydrate'] +` </td>
      </tr>
      <tr>
      <td class = "col-4">Dietary fiber:</td>
      <td class = "col-2 align_me" >`+ data['nf_dietary_fiber'] +` </td>
      </tr>
      <tr>
      <td class = "col-4">Sugar:</td>
      <td class = "col-2 align_me" >`+ data['nf_sugars'] +` </td>
      </tr>
      <tr>
      <td class = "col-4">Potassium:</td>
      <td class = "col-2 align_me" >`+ data['nf_potassium'] +` </td>
      </tr>
    </tbody>
  </table>

    `
    return row;
}


