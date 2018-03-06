import numpy as np
import matplotlib.pyplot as plt

Tasks=["2","3","4","6"]
for task in Tasks:
    colors=["red","green","blue","black","orange","grey","purple","saddlebrown","maroon","tomato"]
    Markers=["o","^","s","p","D","v","*","<","+",">"]
    fig, ax = plt.subplots()
    nupdates = 93587 / 32

    """
    file1 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.03_decay1_decint1000_thr300_allcandn_reg0.1_RFlr0.0001_REINFORCE.result',"r")
    if task=="6":
        file2 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.4_lf0n.result',"r")
    else:
        file2 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.5_lf0n.result',"r")
    file3 = open('task'+task+'_modelFP_sbsz32_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
            
    lines1 = file1.readlines()
    data1 = np.loadtxt(lines1)
    lines2 = file2.readlines()
    data2 = np.loadtxt(lines2)
    lines3 = file3.readlines()
    data3 = np.loadtxt(lines3)

    x1 = data1[3:122:2,0] / (1.0 * nupdates)
    y1 = data1[3:122:2,1]
    x2 = data2[3:122:2,0] / (1.0 * nupdates)
    y2 = data2[3:122:2,1]
    x3 = data3[3:122:2,0] / (1.0 * nupdates)
    y3 = data3[3:122:2,1]

    ax.plot(x1, y1, '-', linewidth=4, markersize=10, color=colors[0], label='REINFORCE', marker=Markers[0])
    ax.plot(x2, y2, '-', linewidth=4, markersize=10, color=colors[1], label='RBI', marker=Markers[1])
    ax.plot(x3, y3, '-', linewidth=2, markersize=10, color=colors[2], label='FP', marker=Markers[2])

    plt.ylabel('Accuracy', fontsize=24)
    plt.xlabel('Epoch', fontsize=24)
    plt.title('Comparing RBI, FP and REINFORCE',fontsize=22)
    plt.legend(loc='lower right', fontsize=18)
    plt.grid(True)
    plt.axis('tight')
#ax.set_xticks(np.arange(0,21,5))
    ax.tick_params(axis='x', labelsize=18)
    ax.tick_params(axis='y', labelsize=18)
    fig.savefig('comparison'+task+'.pdf', format='PDF', bbox_inches='tight')
    plt.show()

# carying exploration

    file1 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0_lf0n.result',"r")
    file2 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.1_lf0n.result',"r")
    file3 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.2_lf0n.result',"r")
    file4 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.3_lf0n.result',"r")
    file5 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.4_lf0n.result',"r")
    if task=="6":
        file6 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.4_lf0n.result', 'r')
    else:
        file6 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.5_lf0n.result', 'r')
    print(file6)
    file7 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps1_lf0n.result', 'r')
    lines1 = file1.readlines()
    data1 = np.loadtxt(lines1)
    lines2 = file2.readlines()
    data2 = np.loadtxt(lines2)
    lines3 = file3.readlines()
    data3 = np.loadtxt(lines3)
    lines4 = file4.readlines()
    data4 = np.loadtxt(lines4)
    lines5 = file5.readlines()
    data5 = np.loadtxt(lines5)
    lines6 = file6.readlines()
    data6 = np.loadtxt(lines6)
    lines7 = file7.readlines()
    data7 = np.loadtxt(lines7)
    fig, ax = plt.subplots()
    x1 = data1[:122:4,0] / (1.0 * nupdates)
    y1 = data1[:122:4,1]
    x2 = data2[:122:4,0] / (1.0 * nupdates)
    y2 = data2[:122:4,1]
    x3 = data3[:122:4,0] / (1.0 * nupdates)
    y3 = data3[:122:4,1]
    x4 = data4[:122:4,0] / (1.0 * nupdates)
    y4 = data4[:122:4,1]
    x5 = data5[:122:4,0] / (1.0 * nupdates)
    y5 = data5[:122:4,1]
    x6 = data6[:122:4,0] / (1.0 * nupdates)
    y6 = data6[:122:4,1]
    x7 = data7[:122:4,0] / (1.0 * nupdates)
    y7 = data7[:122:4,1]

    ax.plot(x1, y1, '-', linewidth=4, markersize=10, color=colors[0], label=r"$\epsilon$=0", marker=Markers[0])
    ax.plot(x2, y2, '-', linewidth=4, markersize=10, color=colors[1], label=r"$\epsilon$=0.1", marker=Markers[1])
    ax.plot(x3, y3, '-', linewidth=4, markersize=10, color=colors[2], label=r"$\epsilon$=0.2", marker=Markers[2])
    ax.plot(x4, y4, '-', linewidth=4, markersize=10, color=colors[3], label=r"$\epsilon$=0.3", marker=Markers[3])
    ax.plot(x5, y5, '-', linewidth=4, markersize=10, color=colors[4], label=r"$\epsilon$=0.4", marker=Markers[4])
    ax.plot(x6, y6, '-', linewidth=4, markersize=10, color=colors[5], label=r"$\epsilon$=0.5", marker=Markers[5])
    ax.plot(x7, y7, '-', linewidth=4, markersize=10, color=colors[6], label=r"$\epsilon$=1", marker=Markers[6])
    plt.title('Random Exploration for RBI',fontsize=22)
    plt.ylabel('Accuracy', fontsize=24)
    plt.xlabel('Epoch', fontsize=24)
    plt.legend(loc='lower right', fontsize=18)
    plt.grid(True)
    plt.axis('tight')
#ax.set_xticks(np.arange(0,21,5))
    ax.tick_params(axis='x', labelsize=18)
    ax.tick_params(axis='y', labelsize=18)
    fig.savefig('RBI'+task+'.pdf', format='PDF', bbox_inches='tight')
    plt.show()



    file1 = open('task'+task+'_modelFP_sbsz32_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0balancenNhop1.result',"r")
    file2 = open('task'+task+'_modelFP_sbsz32_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.1balancenNhop1.result',"r")
    file3 = open('task'+task+'_modelFP_sbsz32_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.2balancenNhop1.result',"r")
    file4 = open('task'+task+'_modelFP_sbsz32_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.3balancenNhop1.result',"r")
    file5 = open('task'+task+'_modelFP_sbsz32_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.4balancenNhop1.result',"r")
    file6 = open('task'+task+'_modelFP_sbsz32_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
    file7 = open('task'+task+'_modelFP_sbsz32_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps1balancenNhop1.result',"r")
    lines1 = file1.readlines()
    data1 = np.loadtxt(lines1)
    lines2 = file2.readlines()
    data2 = np.loadtxt(lines2)
    lines3 = file3.readlines()
    data3 = np.loadtxt(lines3)
    lines4 = file4.readlines()
    data4 = np.loadtxt(lines4)
    lines5 = file5.readlines()
    data5 = np.loadtxt(lines5)
    lines6 = file6.readlines()
    data6 = np.loadtxt(lines6)
    lines7 = file7.readlines()
    data7 = np.loadtxt(lines7)
    fig, ax = plt.subplots()
    x1 = data1[:122:4,0] / (1.0 * nupdates)
    y1 = data1[:122:4,1]
    x2 = data2[:122:4,0] / (1.0 * nupdates)
    y2 = data2[:122:4,1]
    x3 = data3[:122:4,0] / (1.0 * nupdates)
    y3 = data3[:122:4,1]
    x4 = data4[:122:4,0] / (1.0 * nupdates)
    y4 = data4[:122:4,1]
    x5 = data5[:122:4,0] / (1.0 * nupdates)
    y5 = data5[:122:4,1]
    x6 = data6[:122:4,0] / (1.0 * nupdates)
    y6 = data6[:122:4,1]
    x7 = data7[:122:4,0] / (1.0 * nupdates)
    y7 = data7[:122:4,1]

    ax.plot(x1, y1, '-', linewidth=4, markersize=10, color=colors[0], label=r"$\epsilon$=0", marker=Markers[0])
    ax.plot(x2, y2, '-', linewidth=4, markersize=10, color=colors[1], label=r"$\epsilon$=0.1", marker=Markers[1])
    ax.plot(x3, y3, '-', linewidth=4, markersize=10, color=colors[2], label=r"$\epsilon$=0.2", marker=Markers[2])
    ax.plot(x4, y4, '-', linewidth=4, markersize=10, color=colors[3], label=r"$\epsilon$=0.3", marker=Markers[3])
    ax.plot(x5, y5, '-', linewidth=4, markersize=10, color=colors[4], label=r"$\epsilon$=0.4", marker=Markers[4])
    ax.plot(x6, y6, '-', linewidth=4, markersize=10, color=colors[5], label=r"$\epsilon$=0.5", marker=Markers[5])
    ax.plot(x7, y7, '-', linewidth=4, markersize=10, color=colors[6], label=r"$\epsilon$=1", marker=Markers[6])
    plt.ylabel('Accuracy', fontsize=24)
    plt.xlabel('Epoch', fontsize=24)
    plt.legend(loc='lower right', fontsize=18)
    plt.grid(True)
    plt.axis('tight')
#ax.set_xticks(np.arange(0,21,5))
    ax.tick_params(axis='x', labelsize=18)
    ax.tick_params(axis='y', labelsize=18)
    plt.title('Random Exploration for FP',fontsize=22)
    fig.savefig('FP'+task+'.pdf', format='PDF', bbox_inches='tight')
    plt.show()

# Vary simulator batch size

    if task=="6":
        file1 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.4_lf0n.result',"r")
    else:
        file1 = open('task'+task+'_modelRBI_sbsz32_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.5_lf0n.result',"r")
    file2 = open('task'+task+'_modelRBI_sbsz320_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.5_lf0n.result',"r")
    file3 = open('task'+task+'_modelRBI_sbsz3200_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.5_lf0n.result',"r")
    file4 = open('task'+task+'_modelRBI_sbsz32000_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.5_lf0n.result',"r")
    file5 = open('task'+task+'_modelRBI_sbsz93587_mbsz32_lr0.1_decay1_decint1000_thr50_allcandn_eps0.5_lf0n.result',"r")
    lines1 = file1.readlines()
    data1 = np.loadtxt(lines1)
    lines2 = file2.readlines()
    data2 = np.loadtxt(lines2)
    lines3 = file3.readlines()
    data3 = np.loadtxt(lines3)
    lines4 = file4.readlines()
    data4 = np.loadtxt(lines4)
    lines5 = file5.readlines()
    data5 = np.loadtxt(lines5)
    fig, ax = plt.subplots()
    x1 = data1[3:122:4,0] / (1.0 * nupdates)
    y1 = data1[3:122:4,1]
    x2 = data2[3:122:4,0] / (1.0 * nupdates)
    y2 = data2[3:122:4,1]
    x3 = data3[3:122:4,0] / (1.0 * nupdates)
    y3 = data3[3:122:4,1]
    x4 = data4[3:122:4,0] / (1.0 * nupdates)
    y4 = data4[3:122:4,1]
    x5 = data5[3:122:4,0] / (1.0 * nupdates)
    y5 = data5[3:122:4,1]
    ax.plot(x1, y1, '-', linewidth=4, markersize=10, color=colors[0], label='batch 32', marker=Markers[0])
    ax.plot(x2, y2, '-', linewidth=4, markersize=10, color=colors[1], label='batch 320', marker=Markers[1])
    ax.plot(x3, y3, '-', linewidth=4, markersize=10, color=colors[2], label='batch 3200', marker=Markers[2])
    ax.plot(x4, y4, '-', linewidth=4, markersize=10, color=colors[3], label='batch 32000', marker=Markers[3])
    ax.plot(x5, y5, '-', linewidth=4, markersize=10, color=colors[4], label='full dataset', marker=Markers[4])
    plt.ylabel('Accuracy', fontsize=24)
    plt.xlabel('Epoch', fontsize=24)
    plt.legend(loc='lower right', fontsize=18)
    plt.grid(True)
    plt.axis('tight')
#ax.set_xticks(np.arange(0,21,5))
    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20)
    plt.title('RBI (eps=0.5) Varying Batch Size',fontsize=22)
    fig.savefig('batch_RBI_task'+task+'.pdf', format='PDF', bbox_inches='tight')
    plt.show()

    """



    file1 = open('task'+task+'_modelFP_sbsz32_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
    file2 = open('task'+task+'_modelFP_sbsz320_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
    file3 = open('task'+task+'_modelFP_sbsz3200_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
    file4 = open('task'+task+'_modelFP_sbsz32000_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
    file5 = open('task'+task+'_modelFP_sbsz93568_mbsz32_lr0.2_decay1_decint1000_thr50_allcandn_eps0.5balancenNhop1.result',"r")
            
    lines1 = file1.readlines()
    data1 = np.loadtxt(lines1)
    lines2 = file2.readlines()
    data2 = np.loadtxt(lines2)
    lines3 = file3.readlines()
    data3 = np.loadtxt(lines3)
    lines4 = file4.readlines()
    data4 = np.loadtxt(lines4)
    lines5 = file5.readlines()
    data5 = np.loadtxt(lines5)
    fig, ax = plt.subplots()
    x1 = data1[3:122:4,0] / (1.0 * nupdates)
    y1 = data1[3:122:4,1]
    x2 = data2[3:122:4,0] / (1.0 * nupdates)
    y2 = data2[3:122:4,1]
    x3 = data3[3:122:4,0] / (1.0 * nupdates)
    y3 = data3[3:122:4,1]
    x4 = data4[3:122:4,0] / (1.0 * nupdates)
    y4 = data4[3:122:4,1]
    x5 = data5[3:122:4,0] / (1.0 * nupdates)
    y5 = data5[3:122:4,1]
    ax.plot(x1, y1, '-', linewidth=4, markersize=10, color=colors[0], label='batch 32', marker=Markers[0])
    ax.plot(x2, y2, '-', linewidth=4, markersize=10, color=colors[1], label='batch 320', marker=Markers[1])
    ax.plot(x3, y3, '-', linewidth=4, markersize=10, color=colors[2], label='batch 3200', marker=Markers[2])
    ax.plot(x4, y4, '-', linewidth=4, markersize=10, color=colors[3], label='batch 32000', marker=Markers[3])
    ax.plot(x5, y5, '-', linewidth=4, markersize=10, color=colors[4], label='full dataset', marker=Markers[4])
    plt.ylabel('Accuracy', fontsize=24)
    plt.xlabel('Epoch', fontsize=24)
    plt.legend(loc='lower right', fontsize=18)
    plt.grid(True)
    plt.axis('tight')
#ax.set_xticks(np.arange(0,21,5))
    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20)
    plt.title('FP (eps=0.5) Varying Batch Size Task'+task,fontsize=22)
    fig.savefig('batch_FP_task'+task+'.pdf', format='PDF', bbox_inches='tight')
    plt.show()
