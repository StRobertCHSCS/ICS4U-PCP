using UnityEngine;
using System.Collections;

public class Kill_Player : MonoBehaviour {

    // call Level_manager script and set it to variable
    public Level_manager level_manager;

    // Use this for initialization
	void Start () {
        level_manager = FindObjectOfType<Level_manager>();
	}
	
	// Update is called once per frame
	void Update () {
	
	}

    // check if the respawn collider meets player
    void OnTriggerEnter2D(Collider2D collide)
    {
        if(collide.name == "Scorpion")
        {
            level_manager.Respawn_Player();
        }
    }
}
