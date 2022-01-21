for i=1:length(t)
%     punto = R.fkine(q_ctraj(i,:));
    poses=UR3.ikunc(transl(curve_x(i)+trajOrigin_x,curve_y(i)+trajOrigin_y,curve_z(i)+trajOrigin_z)*troty(45+180,'deg')*trotz(90,'deg'));
    hold on
    plot3(side_x+trajOrigin_x,side_1y+trajOrigin_y,sides_z+trajOrigin_z)
%     dosR.plot(q_ctraj(i,:))
%     plot3(punto(1,4),punto(2,4),punto(3,4),'r*')
    %view(3)
    UR3.plot(poses,'workspace',[-0.4 0.4 -0.4 0.4 0 0.8]);
    view([35.199 30.545])
    %pause(0.5)
end
