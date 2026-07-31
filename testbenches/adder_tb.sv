module adder_tb();

logic [3:0] a;
logic [3:0] b;
logic [4:0] sum;
logic clk=0;

integer i;
integer j;
integer pass_count;
integer fail_count;

// module instantiation module_name instance_name
adder dut(.a, .b, .sum);

//initial begin
//    clk = 0;
//end

always
    #50 clk = ~clk;

initial begin
    i = 0;
    j = 0;
    pass_count = 0;
    fail_count = 0;
    a = 0;
    b = 0;
end

always @(posedge clk)begin

    if (sum == (i+j)) begin
        pass_count++;
    end
    else begin
        fail_count++;
        $display("FAIL: a=%0d, b=%0d, expected=%0d, actual=%0d", a, b, (i+j), sum);
    end

    if (i == 15 && j == 15) begin
        $display("Passed: %0d", pass_count);
        $display("Failed: %0d", fail_count);
        $finish;
    end
    else if (j < 15) begin
        j++;
        b = j;
    end
    else begin
        j = 0;
        i++;
        a = i;
        b = j;
    end

end

endmodule: adder_tb