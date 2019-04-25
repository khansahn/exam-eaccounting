///////////////////////// CASHFLOW HISTORY ////////////////////////////////


// ============================================HISTORY FORM============GET ALL CASHFLOW HISTORY
$.ajax({
    url: 'http://10.10.100.152:5050/cashflow/getAll',
    method : 'GET',
    async:true,    
    success: function(result){
        var tabel =""
        for (let i=0; i<result.data.length; i++){           
            $("#tabelListHistory").append(
                `<tr>
                <td>`+(i+1)+`</td>
                <td>`+result.data[i].keterangan+`</td>
                <td>`+result.data[i].created_at+`</td>
                <td>`+result.data[i].cash_in+`</td>
                <td>`+result.data[i].cash_out+`</td>
                <td>`+result.data[i].balance+`</td>
                </tr>`
                )
                
            } 
        },
        error : function(){
            // error handling
        },
        complete: function(){
            
        },
        statusCode: {
            403: function() {
                window.location.href = 'index.html'
            }
        }
    })
    
    //////////////////////////// PENJUALAN BARANG /////////////////////////////
    
    // =================================================GET ALL BARANG
    $.ajax({
        url: 'http://10.10.100.152:5050/master/barang/getAll',
        method : 'GET',
        async:true,
        success: function(result){
            listPosisi = ""
            $("#listBarang").append("<option value="+0+">"+"Pilih Barang"+"</option>")
            for (let i=0; i<result.data.length; i++){
                $("#listBarang").append("<option value="+result.data[i].id+">"+result.data[i].name+"</option>")
            }
            
        },
        error : function(){
            alert("transaksi gagal")
        },
        complete: function(){
            
        },
        statusCode: {
            403: function() {
                window.location.href = 'index.html'
            }
        }
    })
    
    
    
    
    // =============================================================SUBMIT PENJUALAN==================
    function submitPenjualan() {
        var nama_penjualan = document.getElementById("penjualan-name").value;
        var id_barang = document.getElementById("listBarang").value;
        var jumlah_terjual = document.getElementById("penjualan-jumlah").value;
        
        $.ajax({
            url:'http://10.10.100.152:5050/transaksi/penjualanBarang',
            method: 'POST',
            async:true,
            contentType: 'application/json',
            data: JSON.stringify({
                "nama_penjualan": nama_penjualan,
                "id_barang": id_barang,
                "jumlah_terjual": parseInt(jumlah_terjual)
                
            }),
            success: function(result) {
                console.log(result)
                alert("Anda berhasil submit")
                window.location.href = 'index.html'
            },
            error: function(error){
                alert("Submit error")
            },
            complete: function() {
                
            },
            statusCode: {
                403: function() {
                    window.location.href = 'index.html'
                }
            }
        })
    }
    
    
    ///////////////////////////// PEMBELIAN BARANG /////////////////////////
    
    
    
    // =============================================================SUBMIT PENJUALAN==================
    function submitPembelian() {
        var nama_pembelian = document.getElementById("pembelian-name").value;
        var nama_barang = document.getElementById("pembelian-barang-name").value;
        var satuan = document.getElementById("pembelian-barang-satuan").value;
        var jumlah = document.getElementById("pembelian-jumlah").value;
        var harga_beli = document.getElementById("pembelian-hb").value;
        var harga_jual = document.getElementById("pembelian-hj").value;
        
        
        $.ajax({
            url:'http://10.10.100.152:5050/transaksi/pembelianBarang',
            method: 'POST',
            async:true,
            contentType: 'application/json',
            data: JSON.stringify({
                "nama_pembelian": nama_pembelian,
                "nama_barang": nama_barang,
                "satuan": satuan,
                "jumlah": parseInt(jumlah),
                "harga_beli": parseFloat(harga_beli),
                "harga_jual": parseFloat(harga_jual)  
            }),
            success: function(result) {
                console.log(result)
                alert("Anda berhasil submit")
                window.location.href = 'index.html'
            },
            error: function(error){
                alert("Submit error")
            },
            complete: function() {
                
            },
            statusCode: {
                403: function() {
                    window.location.href = 'index.html'
                }
            }
        })
    }