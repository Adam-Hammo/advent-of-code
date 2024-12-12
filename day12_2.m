clear

Lines = strsplit(fileread('day12.txt'), '\n');
nr = numel(Lines);
nc = max(cellfun('length', Lines));
Garden = repmat(' ', nr, nc);
for i = 1:nr
    Garden(i, 1:length(Lines{i})) = Lines{i};
end

s = 0;
Plants = unique(Garden);
for plant = Plants'
    % Make image bigger to counter non-linear algos lol
    Patches = padarray(imresize(Garden==plant, 4, 'nearest'), [2 2], 0, 'both');
    
    CC = bwconncomp(Patches,4);
    for i = 1:CC.NumObjects
        Patch = false(size(Patches));
        Patch(CC.PixelIdxList{i}) = true;
        Edges = edge(Patch, 'sobel', 0.001);
        
        runstarts = @(v) find(diff([0 v 0])==1);
        runends   = @(v) find(diff([0 v 0])==-1)-1;
        countEdges = @(v) sum((runends(v)-runstarts(v)+1)>=2);

        totalEdges = sum(arrayfun(@(r)countEdges(Edges(r,:)),1:size(Edges,1))) + sum(arrayfun(@(c)countEdges(Edges(:,c)'),1:size(Edges,2)));
        area = sum(sum(Patch))/16;
        
        s = s + totalEdges*area;
    end
end
s