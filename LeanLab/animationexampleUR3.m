anim = Animate('movie');
for i=1:length(t)*4
%     punto = R.fkine(q_ctraj(i,:));
    poses=UR3.ikunc(transl(trayectoria_Final_x(i)+trajOrigin_x,trayectoria_Final_y(i)+trajOrigin_y,trayectoria_Final_z(i)+trajOrigin_z)*troty(45+180,'deg')*trotz(90,'deg'));
    hold on
    plot3(0.1,0.1,0.7)
%     dosR.plot(q_ctraj(i,:))
%     plot3(punto(1,4),punto(2,4),punto(3,4),'r*')
    %view(3)
    UR3.plot(poses,'workspace',[0 0.5 0 0.5 0 0.8],'fps',60);
    anim.add();
    view([45 45])
    %pause(0.01)

    
end
