fid = fopen('day13.txt', 'r');
parseLine = @(line) regexp(line, 'X[+=](\d+),\s*Y[+=](\d+)', 'tokens', 'once');
cost = 0;
while true
    lineA = fgetl(fid);
    if isempty(strtrim(lineA))
        lineA = fgetl(fid);
        if ~ischar(lineA), break; end
    end
    lineB = fgetl(fid);
    lineP = fgetl(fid);
    
    tokensA = parseLine(lineA);
    tokensB = parseLine(lineB);
    tokensP = parseLine(lineP);

    syms a b;
    X = a*str2num(tokensA{1}) + b*str2num(tokensB{1}) == 10000000000000+str2num(tokensP{1});
    Y = a*str2num(tokensA{2}) + b*str2num(tokensB{2}) == 10000000000000+str2num(tokensP{2});

    turns = solve(X,Y);
    if mod(turns.a,1)==0 && mod(turns.b,1)==0
        cost = cost + subs(3*a + b, turns);
    end
end
cost