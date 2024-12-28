clear

Lines = strsplit(fileread('day8.txt'), '\n');
nr = numel(Lines);
nc = max(cellfun('length', Lines));
Antennas = repmat(' ', nr, nc);
for i = 1:nr
    Antennas(i, 1:length(Lines{i})) = Lines{i};
end
Frequencies = unique(Antennas(Antennas~=char(".")));
Antinodes = false(size(Antennas));
for f = Frequencies'
    [Y, X] = find(Antennas == f);
    Pairs = nchoosek(1:numel(Y), 2);
    Y1 = Y(Pairs(:,1)); X1 = X(Pairs(:,1)); Y2 = Y(Pairs(:,2)); X2 = X(Pairs(:,2));
    M = (Y2-Y1)./(X2-X1);
    B = Y1 - M.*X1;
    X = repmat(1:nc, size(Pairs, 1), 1);
    CandidateY = M.*X+B;
    ValidMask = (mod(X - repmat(X1, 1, nc), repmat(abs(X2 - X1), 1, nc)) == 0) & isbetween(CandidateY, 1, nc);
    Antinodes(round(sub2ind([nr, nc], X(ValidMask), CandidateY(ValidMask)))) = true;
end
sum(sum(Antinodes))