clear
w=101;h=103;
for t = 1:100000
    fid = fopen('day14.txt', 'r');
    line = fgetl(fid);
    P=zeros(h,w);
    while ischar(line)
        robot = sscanf(line, 'p=%f,%f v=%f,%f');
        px = mod(robot(1)+robot(3)*t,w)+1;
        py = mod(robot(2)+robot(4)*t,h)+1;
        P(py,px) = P(py,px) + 1;
        line = fgetl(fid);
    end
    % Part 2: assume no overlaps is a good guess and visualise it
    if max(max(P))==1
        imshow(P==0);
        disp(t)
    end
end

% Part 1 (no outer loop above, t=100)
xm=(w+1)/2;ym=(h+1)/2;
sum(sum(P(1:ym-1, 1:xm-1)))*sum(sum(P(1:ym-1, xm+1:end)))*sum(sum(P(ym+1:end, 1:xm-1)))*sum(sum(P(ym+1:end, xm+1:end)))