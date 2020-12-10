let {investir} = require("../controller/investirController");
let $ = require("jquery");
$(document).ready(function () {
  let periodoTaxa  = "mês";
  let periodoTempo = "meses";
  let periodoResgate = "meses";

  $("div.campo input[type=radio]").change(function(){
    let tipo = $('input[name=tipo]:checked').val();
    if(tipo=="ano"){    
      periodoTempo ="anos";
    }else if(tipo=="mes"){
      $("#despositos-mensais").fadeIn();
      periodoTempo = "meses";
    }
    $("#periodoTaxa").html(periodoTaxa);
    $("#periodoTempo").html(periodoTempo);
  });
  
  $('#simulador').on('submit', function (event) {
    event.preventDefault();
  });

  let simular = function(){
    let valor    = $("#valor").val();
    let deposito = $("#deposito").val();
    let taxa     = $("#taxa").val();
    let parcelas = $("#parcelas").val();
    let tipoPeriodo = $('input[name=tipo]:checked').val();
    if(deposito==""){
      deposito = 0;
    }
     if(valor!=="" && taxa!=="" && parcelas!==""){
       if(tipoPeriodo==="ano"){
         periodoTaxa  = "mês";
         periodoTempo ="ano";
         periodoResgate = (parcelas>1)?parcelas+" anos":parcelas+" ano";
         parcelas = parcelas*12;

       }else if(tipoPeriodo==="mes"){
         periodoTaxa  = "mês";
         periodoTempo = "meses";
         periodoResgate = (parcelas>1)?parcelas+" meses":parcelas+" mês";
       }
        let simulador = new investir(valor, deposito, taxa, parcelas, tipoPeriodo);
            simulador.tratarMascaraReal();
            simulador.formataDados(); 
              let valorResgatado = simulador.valorResgatado();
              let investido = parseFloat(valor)+(parseFloat(deposito)*parseInt(parcelas));
              let redimentoJuros = simulador.vF-investido;
                  investido = simulador.formataMascara('BRL',investido);
                  redimentoJuros = simulador.formataMascara('BRL',redimentoJuros);
              $("#resultado").html("");
              $("#resultado").append("<h2>RESGATE DO DE INVESTIMENTO EM "+periodoResgate+"</h2><br>");
              $("#resultado").append("O valor investido foi de "+investido+"<hr>");
              $("#resultado").append("Os juros recebidos foram de "+redimentoJuros+"<hr>");
              $("#resultado").append("O Investimento Resgatado é "+valorResgatado+"<hr>");
              $("#resultado").append("Com Taxa de Juros de "+taxa+"% ao "+periodoTaxa+". <hr>");
              $("#resultado").append("Com depósitos Mensais de: "+simulador.getDm()+"<hr>");

     }else{
         alert("Preencha o valor, a taxa e o tempo de investimento!");
     }
  };
  $(document).keypress(function(e) {
     if(e.which == 13) {
       $("#simulador").submit();
       simular();
     }
   });

   $("#simular").click(function(){
     simular();
   });
   
   
   });
