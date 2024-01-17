program tictactoe(input, output);

const BOARD_SIZE: Integer = 3;
const PInfinity: Real = 1.0 / 0.0;
const NInfinity: Real = -1.0 / 0.0;

type Board = Array of Array of Char;

// Tuple
type Int2Tuple = record
    Item1, Item2: Integer;
end;

procedure InitBoard(var board: Board);
var i, j: Integer;
begin 
    SetLength(board, BOARD_SIZE, BOARD_SIZE);
    for i := 0 to BOARD_SIZE - 1 do 
        for j := 0 to BOARD_SIZE - 1do 
            board[i, j] := '?';
end;

function Max(x, y: Real): Real;
var result: Real;
begin 
    if x > y then 
        result := x
    else result := y;
    Max := result;
end;

function Min(x, y: Real): Real;
var result: Real;
begin 
    if x < y then 
        result := x
    else result := y;
    Min := result;
end;

function Equals3(x, y, z: Char): Boolean;
begin
    equals3 := (x = y) and (y = z) and (x <> '?');
end;

function CheckWinner(board: Board): Char;
var winner: Char;
var i, j: Integer;
var openSlots: Integer;
begin
    winner := 'N';
    openSlots := 0;
    for i := 0 to BOARD_SIZE - 1 do 
    begin
        if equals3(board[i, 0], board[i, 1], board[i, 2]) then 
            winner := board[i, 0];
    end;
    for i := 0 to BOARD_SIZE - 1 do 
    begin 
        if equals3(board[0, i], board[1, i], board[2, i]) then 
            winner := board[0, i];
    end;
    // check diagonally
    if equals3(board[0, 0], board[1, 1], board[2, 2]) then 
        winner := board[0, 0];
    if equals3(board[0, 2], board[1, 1], board[2, 0]) then 
        winner := board[0, 2];
    
    for i := 0 to BOARD_SIZE - 1 do 
    begin 
        for j := 0 to BOARD_SIZE - 1 do 
        begin 
            if board[i, j] = '?' then 
                openSlots := openSlots + 1;
        end;
    end;

    if (winner = 'N') and (openSlots = 0) then 
        Exit('T')
    else 
        Exit(winner);
end;

function Minimax(var board: Board; isMaxPlayer: Boolean; turn: Char): Real;
var bestScore, score: Real;
var i, j: Integer;
var result: Char;
begin
    result := CheckWinner(board);
    if result <> 'N' then 
    begin
        if result = 'X' then Exit(1.0)
        else if result = 'O' then Exit(-1.0)
        else if result = 'T' then Exit(0.0);
    end;

    if isMaxPlayer then
    begin 
        bestScore := NInfinity;
        for i := 0 to BOARD_SIZE - 1 do 
        begin 
            for j := 0 to BOARD_SIZE - 1 do
            begin 
                if board[i, j] = '?' then 
                begin
                    board[i, j] := turn;
                    score := minimax(board, False, 'O');
                    board[i, j] := '?';
                    bestScore := Max(score, bestScore);
                end;
            end;
        end;
        Exit(bestScore);
    end
    else 
    begin 
        bestScore := PInfinity;
        for i := 0 to BOARD_SIZE - 1 do 
        begin 
            for j := 0 to BOARD_SIZE - 1 do
            begin 
                if board[i, j] = '?' then 
                begin
                    board[i, j] := turn;
                    score := minimax(board, True, 'X');
                    board[i, j] := '?';
                    bestScore := Min(score, bestScore);
                end;
            end;
        end;
        Exit(bestScore);
    end;
end;

procedure HumanMove(var board: Board);
var x, y: Integer;
var code: Integer;
begin
    while True do 
    begin 
        writeln('Place O in:');
        write('X: ');
        readln(x);
        write('Y: ');
        readln(y);
        if (x >= 0) or (x < 3) or (y >= 0) or (y < 3) then 
        begin 
            if board[x, y] = '?' then 
            begin
                board[x, y] := 'O';
                break;
            end
            else 
                writeln('Invalid move. Place O in an empty cell.');
        end
        else 
            writeln('Invalid move. Index out of bounds.');
    end;
    writeln();
end;

procedure ComputerMove(var board: Board);
var bestMove: Int2Tuple;
var bestScore, score: Real;
var i, j: Integer;
begin
    bestMove.Item1 := 0;
    bestMove.Item2 := 0;
    bestScore := NInfinity;
    for i := 0 to BOARD_SIZE - 1 do 
    begin 
        for j := 0 to BOARD_SIZE - 1 do 
        begin 
            if board[i, j] = '?' then 
            begin 
                board[i, j] := 'X';
                score := Minimax(board, False, 'O');
                board[i, j] := '?';
                if score > bestScore then 
                begin 
                    bestScore := score;
                    bestMove.Item1 := i;
                    bestMove.Item2 := j;
                end;
            end;
        end;
    end;
    board[bestMove.Item1, bestMove.Item2] := 'X'; 
end;

procedure PrintBoard(board: Board);
var i, j: Integer;
begin
    for i := 0 to BOARD_SIZE - 1 do 
    begin
        for j := 0 to BOARD_SIZE - 1 do 
            write(board[i, j], ' ');
        writeln();
    end;
end;

var b: Board;
var winner: Char;
begin
    InitBoard(b);
    winner := 'N';
    while winner = 'N' do 
    begin
        ComputerMove(b);
        PrintBoard(b);
        HumanMove(b);
        winner := CheckWinner(b);
    end;
    writeln();
    PrintBoard(b);
end.