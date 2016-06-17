using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class EnemyHealthScript : MonoBehaviour {
	public int health;

	// Use this for initialization
	void Start () {
	}

	// Update is called once per frame
	void Update () {
		if (health < 1) {
			foreach (Transform child in this.transform) {
				Destroy (child.gameObject);
			}
			Destroy (this.gameObject);
		}



		}

	

}
